import heapq
n,k = map(int,input().split())
ab = [0]*n
lis = []
for i in range(n):
    a,b = map(int,input().split())
    lis.append([a,b])
lis.sort(key= lambda val : val[0])
c = 0
for a,b in lis:
    if k <= c+b:
        ans = a
        break
    else:
        c += b
print(ans)