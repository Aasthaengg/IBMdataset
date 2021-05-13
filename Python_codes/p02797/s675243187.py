import sys
input = sys.stdin.readline

n, k, s = [int(x) for x in input().split()]

ans = [s]*k
add = s + 1 if s + 1 <= 10**9 else s - 1
for i in range(n - len(ans)):
    ans.append(add)
print(*ans)


