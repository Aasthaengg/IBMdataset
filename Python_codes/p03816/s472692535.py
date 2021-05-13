n = int(input())
a = sorted(list(map(int, input().split())))

eat = 0
l = 0
r = n-1
while l < r:
    while l < n - 1 and a[l+1] != a[l]:
        l += 1
    while r > 0 and a[r-1] != a[r]:
        r -= 1
    if r <= l:
        break
    eat += 1
    l += 1
    r -= 1
print(n-eat*2)