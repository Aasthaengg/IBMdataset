import sys

input = sys.stdin.buffer.readline
n = int(input())
S = []
for _ in range(n):
    S.append(int(input()))
S.sort()
goukei = sum(S)
if goukei %10!=0:
    print(goukei)
    exit()
ans = 0
for i in range(n):
    temp = goukei - S[i]
    if temp % 10 == 0:
        temp = 0
    ans = max(ans, temp)

print(ans)
