n=int(input())
a=input()
b=input()
c=input()
r=0
for x in range(n):
    r+=len(set(a[x]+b[x]+c[x]))-1
print(r)