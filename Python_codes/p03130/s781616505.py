cnt=[0]*4
for i in range(3):
    a,b=map(int,input().split())
    cnt[a-1]+=1
    cnt[b-1]+=1
if 0 in cnt or 3 in cnt:
    print("NO")
else:
    print("YES")