n=int(input())
am,bm=0,10**9
for i in range(n):
    a,b=map(int,input().split())
    am=max(am,a)
    bm=min(bm,b)
print(am+bm)