n = int(input())
a = list(map(int, input().split()))
a.sort()
m = a.pop()
r = m/2

def isOK(index, key):
    return a[index] >= key

def bsearch(key):
    left = -1
    right = n-1

    while right-left > 1:
        mid = left+(right-left)//2
        if isOK(mid, key):
            right = mid
        else:
            left = mid

    if right == n-1:
        return -1
    else:
        return right

index = bsearch(r)

if index > 0 and 2*r < a[index-1]+a[index]:
    index -= 1

print(m, a[index])