N,X=map(int,input().split())
m=[]
for i in range(N):
    m.append(int(input()))

X=X-sum(m)
cnt=len(m)

cnt+=X//min(m)

print(cnt)