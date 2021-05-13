n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

l = 0
r = n

while l < r:
    mid = (l+r)//2

    size = sum(a[:mid+1])
    ptr = mid+1
    ans = True

    while ptr < n:
        if 2*size >= a[ptr]:
            size += a[ptr]
            ptr += 1
        else:
            ans = False
            break

    if ans:
        r = mid
    else:
        l = mid+1

print(n-l)