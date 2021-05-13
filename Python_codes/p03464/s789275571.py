k = int(input())
a = list(map(int, input().split()))[::-1]
l, r = 2, 2
for i in range(k):
    l = ((l-1)//a[i] + 1) * a[i]
    r = (r//a[i] + 1) * a[i] - 1
    if l > r:
        print(-1)
        exit()
print(l, r)
