N=int(input())
s=[list(input()) for _ in range(N)]

for n in range(N):
    s[n].sort()
s.sort()

cnt=[]
i=0
for n in range(1,N):
    if s[n]==s[n-1]:
        i+=1
    else:
        cnt.append(i)
        i=0
if i!=0:
    cnt.append(i)

ans=0
for e in cnt:
    ans+=(e+1)*e//2
print(ans)