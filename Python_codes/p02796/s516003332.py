from operator import itemgetter
N = int(input())
arms = []
finishtime = float('-inf')
ans=[]
for i in range(N):
    x,l = map(int,input().split())
    arms.append((x-l,x+l))
arms.sort(key=itemgetter(1))
for i in range(N):
    if arms[i][0]>=finishtime:
        ans.append(i)
        finishtime = arms[i][1]
print(len(ans))