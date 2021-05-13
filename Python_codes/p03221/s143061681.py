from operator import itemgetter

def id(n):
    if len(str(n)) >= 6:
        return str(n)
    return "0"*(6-len(str(n)))+str(n)

n,m = map(int,input().split())
data = [[] for i in range(n+1)]
for i in range(m):
    p,y = map(int,input().split())
    data[p].append((i,y))
ans = []
for i in range(n+1):
    if data[i]:
        data[i].sort(key=itemgetter(1))
        for j in range(len(data[i])):
            ans.append((data[i][j][0],id(i)+id(j+1)))
ans.sort()
for i,j in ans:
    print(j)