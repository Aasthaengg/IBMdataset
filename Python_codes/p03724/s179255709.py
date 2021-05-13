from collections import defaultdict
n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]
cnt=defaultdict(lambda :0)
for i in range(m):
    cnt[ab[i][0]]+=1
    cnt[ab[i][1]]+=1

for i in cnt.values():
    if i%2!=0:
        print('NO')
        exit()
print('YES')