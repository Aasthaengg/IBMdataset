n = int(input())
a = list(map(int,input().split()))
b = list(a)
b.sort()
l = [b[n//2-1],b[n//2]]
r = [b[n//2],b[n//2-1]]
for i in range(n):
    if a[i] <= l[0]:
        print(l[1])
    else:
        print(r[1])