N,X=map(int,input().split())
m=[int(input()) for i in range(N)]
m.sort()
ans=len(m)
X-=sum(m)
while 0<=X-m[0]:X-=m[0];ans+=1
print(ans)