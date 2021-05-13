n = input()
S = list(map(int, input().split()))
q = input()
T = list(map(int, input().split()))


def solve(s, t):
    cnt = 0
    for i in t:
        if i in s:
            cnt += 1
    return cnt


print(solve(S, T))