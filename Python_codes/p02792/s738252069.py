N=int(input())

cnt=[[0]*10 for _ in range(10)]

for i in range(1,N+1):
    if i%10==0:
      continue
    s=str(i)
    up=int(s[0])
    down=int(s[-1])
    cnt[up][down]+=1

ans=0
for i in range(1,10):
    for j in range(1,10):
        a=cnt[i][j]
        b=cnt[j][i]
        ans+=a*b

print(ans)
