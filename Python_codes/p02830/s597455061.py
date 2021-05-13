n=int(input())
a,b=[str(i) for i in input().split()]
s=''
for i in range(0,len(a)):
    s=s+a[i]+b[i]
print(s)