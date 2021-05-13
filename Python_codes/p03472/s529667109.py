import heapq
n,h= map(int,input().split())
bl = []
heapq.heapify(bl)
maxa = -1
for i in range(n):
    a,b=map(int,input().split())
    maxa=max(maxa,a)
    heapq.heappush(bl,-b)
count=0
while len(bl)>0:
    if -bl[0]>maxa:
        h-=-heapq.heappop(bl)
        count+=1
        if h<=0:break
    else:break
if h<=0:print(count)
else:print(count + h//maxa + (1 if h%maxa>0 else 0))
