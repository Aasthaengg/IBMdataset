import sys
input = lambda: sys.stdin.readline().rstrip()

N,A,B,C = map(int, input().split())
l = [int(input()) for _ in range(N)]

def dfs():
    stack = [(0,0,0,0,0)]
    ans = float("inf")

    while stack:
        current, c_a, c_b, c_c, score = stack.pop()

        if current == N:
            if c_a > 0 and c_b > 0 and c_c > 0:
                ans = min(ans, abs(A - c_a) + abs(B - c_b) + abs(C - c_c) + score - 30)
            continue

        stack.append((current+1, c_a, c_b, c_c, score))
        stack.append((current+1, c_a+l[current], c_b, c_c, score+10))
        stack.append((current+1, c_a, c_b+l[current], c_c, score+10))
        stack.append((current+1, c_a, c_b, c_c+l[current], score+10))

    return ans
print(dfs())