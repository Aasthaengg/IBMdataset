n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
change=[]

for i in range(m):
    b, c=map(int, input().split())
    change.append((c, b))

change.sort(reverse=True)
elem=0

for c, b in change:
    while elem<n and b>0:
        if a[elem]<c:
            a[elem]=c
            b-=1
        elem+=1

print(sum(a))