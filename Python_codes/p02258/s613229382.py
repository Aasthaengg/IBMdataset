n = int(input())

rt = [input() for i in range(n)]

minv = int(rt[0])
maxv = int(rt[1]) - int(rt[0])

for j in range(1,n):
    maxv = max(maxv,int(rt[j]) - minv)
    minv = min(minv,int(rt[j]))

print(maxv)