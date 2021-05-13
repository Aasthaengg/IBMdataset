from bisect import bisect_left as bi
n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
b,num = bi(a,0),a[0]
if b==n:
    q = n-1
    print(a[-1]-sum(a[:n-1]))
elif b:
    q = b
    print(sum(a[b:])-sum(a[:b]))
else:
    q = 1
    print(sum(a[1:])-a[0])
for i in range(q,n-1):
    print(num,a[i])
    num-=a[i]
print(a[-1],num)
num = a[-1]-num
for i in range(1,q):
    print(num,a[i])
    num-=a[i]