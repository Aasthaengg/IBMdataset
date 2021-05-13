N=int(input())
a=list(map(int,input().split()))

b=sum(a)/len(a)
c=[abs(a[i]-b) for i in range(N)]

print(c.index(min(c)))