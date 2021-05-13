N=int(input())
d=list(map(int,input().split()))
d=sorted(d)

d1,d2=d[N//2-1],d[N//2]
print(d2-d1)