n=int(input())
d=list(map(int,input().split()))
a=0
for i in range(n-1):
    a+=d[i]*sum(d[i+1:n])
print(a)