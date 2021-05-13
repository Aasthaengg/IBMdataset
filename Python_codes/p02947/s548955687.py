from sys import stdin
import copy

n = int(input())
S = [stdin.readline()[:-1] for i in [0]*(n)]
#S.append(stdin.readline())
s = []
for i in S:
    s.append("".join(sorted(i)))
s.sort()
arr = []
temp = 1
for i in range(n-1):
    if temp>1 and s[i]!=s[i+1]:
        arr.append(temp)
        temp = 1
    if s[i]==s[i+1]:
        temp += 1
if temp>1:
    arr.append(temp)

ans = 0
for i in arr:
    ans += i*(i-1)//2
print(ans)
