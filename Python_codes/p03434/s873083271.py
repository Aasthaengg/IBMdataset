n=int(input())
a=list(map(int,input().split()))
a_sort=a.sort(reverse=True)
point_a=0
point_b=0
for i in range(0,n,2):
    point_a+=a[i]
for i in range(1,n,2):
    point_b+=a[i]
print(point_a-point_b)