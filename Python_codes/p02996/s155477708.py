n=int(input())
a=[[int(i) for i in input().split()] for _ in range(n)]
a=sorted(a,reverse=True,key=lambda x:x[1])

t=a[0][1]
for x in a:
    t=min(x[1],t)-x[0]
print("Yes" if t>=0 else "No")