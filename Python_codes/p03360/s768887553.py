a = list(map(int, input("").split()))
k=int(input())
m=0
if a[1] >= a[0] or a[2] >= a[0]:
    if a[2] >= a[1]:
        m=2
    else:
        m=1
for i in range(k):
    a[m]=a[m]*2
print(a[0]+a[1]+a[2])