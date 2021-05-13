n,a,b = map(int, input().split())
Alist = list(map(int, input().split())) 


dlist =[0]*(n-1)

for i in range(0,n-1):
    dlist[i] = (Alist[i+1] - Alist[i])*a

res = 0
for i in range(0,n-1):
    if dlist[i] > b:
        res += b
    else:
        res += dlist[i]

print(res)