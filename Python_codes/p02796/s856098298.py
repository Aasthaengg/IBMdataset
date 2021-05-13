from operator import itemgetter
N = int(input())
arms = []
finishtime = float('-inf')
for i in range(N):
    x,l = map(int,input().split())
    arms.append((x-l,x+l))
arms.sort(key=itemgetter(1))
cnt=0
for L,R in arms:
    if finishtime<=L:
        cnt+=1
        finishtime = R
print(cnt)