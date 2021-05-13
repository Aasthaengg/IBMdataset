n,m = map(int,input().split())
lst = [[] for _ in range(8)]
for i in range(n):
    x,y,z = map(int,input().split())
    lst[0].append(x+y+z)
    lst[1].append(x+y-z)
    lst[2].append(x-y+z)
    lst[3].append(x-y-z)
    lst[4].append(-x+y+z)
    lst[5].append(-x+y-z)
    lst[6].append(-x-y+z)
    lst[7].append(-x-y-z)
for i in range(8):
    lst[i].sort(reverse=True)
res = []
for i in range(8):
    res.append(sum(lst[i][:m]))
print(max(res))