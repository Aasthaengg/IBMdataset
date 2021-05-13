import sys
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    A.append([int(x) for x in input().split()])
ans = 0
for i in A:
    ans += i[1] - i[0] + 1
print(ans)