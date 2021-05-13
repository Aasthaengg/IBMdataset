cnt=[0]*4
for i in range(3):
    a,b=map(lambda x:int(x)-1,input().split())
    cnt[a]+=1
    cnt[b]+=1
if max(cnt)<3:
    print('YES')
else:
    print('NO')