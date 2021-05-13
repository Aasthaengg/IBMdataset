n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

a.sort()
f.sort(reverse=True)
lst = []
maxi = 0
for i in range(n):
    lst.append([a[i]*f[i], f[i]])
    maxi = max(maxi, a[i]*f[i])

left = -1 # 不可能
right = maxi # 可能
while left+1 < right:
    mid = (left+right)//2
    cnt = 0
    for i in range(n):
        lsti = lst[i]
        if lsti[0] > mid:
            sa = lsti[0] - mid
            cnt += (sa+lsti[1]-1) // lsti[1]
    if cnt <= k:
        right = mid
    else:
        left = mid
print(right)