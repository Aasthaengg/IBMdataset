N=int(input())
s=input()

W=0
R=0
for i in range(N):
    if s[i]=='R':
        R+=1

count = R

for p in range(N):
    if s[p]=='R':
        R-=1
    elif s[p]=='W':
        W+=1
    if max(R, W) < count:
        count = max(R, W)

print(count)
