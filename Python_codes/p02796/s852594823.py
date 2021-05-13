from operator import itemgetter
N=int(input())
arms=[]
for _ in range(N):
    x,l=map(int,input().split())
    a,b=x-l,x+l
    arms.append([a,b])

arms.sort(key=itemgetter(1))

cnt=1
tmp=arms[0][1]
for arm in arms:
    if arm[0]<tmp: continue
    cnt+=1
    tmp=arm[1]

print(cnt)