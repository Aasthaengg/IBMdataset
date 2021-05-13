n = int(input())
x = [int(i) for i in input().split()]
a = x.copy()
a.sort()
mid = a[int(n/2)-1]
for i in range(n):
    if x[i] <= mid:
        ans = a[int(n/2)]
    else:
        ans = mid
    print(ans)