import bisect
n,m = map(int,input().split())
data = []
for i in range(m):
    data.append(list(map(int,input().split())))
r = sorted(data,key= lambda x:(x[0],x[1]))
o = [[] for _ in range(100001)]

for i in range(m):
    o[r[i][0]].append(r[i][1])

for i in range(m):
    print("0"*(6-len(str(data[i][0]))),end="")
    print(data[i][0],end="")
    num = bisect.bisect_left(o[data[i][0]],data[i][1])+1
    print("0"*(6-len(str(num))),end="")
    print(num)