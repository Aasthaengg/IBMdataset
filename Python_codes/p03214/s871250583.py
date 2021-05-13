n=int(input())
a=list(map(int,input().split()))
s=sum(a)/len(a)
b=[abs(i-s) for i in a]
m=min(b)
print(b.index(m))