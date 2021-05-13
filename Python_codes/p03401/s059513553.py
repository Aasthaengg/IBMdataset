#092_C
n=int(input())
a=[0]+[int(j) for j in input().split()]+[0]
d1=[abs(a[i]-a[i+1]) for i in range(n+1)]
d2=[abs(a[i]-a[i+2]) for i in range(n)]
sum_all=sum(d1)
for i in range(n):
    print(sum_all-d1[i]-d1[i+1]+d2[i])