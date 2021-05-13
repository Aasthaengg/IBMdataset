n,k,s=map(int,input().split())
a=[]
for i in range(k):
    a.append(s)

for i in range(k,n):
    if s!=10**9:
        a.append(10**9)
    else:
        a.append(1)

print(*a)