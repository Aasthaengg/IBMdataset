n = int(input())
a = list(map(int, input().split()))

def ruiseki(a):
    right, left = [], []
    l, r = 0, 0
    for i in range(n):
        l += a[i]
        left.append(l)
    
        r += a[-(i+1)]
        right.append(r)
    return left, right[::-1]

l, r = ruiseki(a)
ans = [abs(l[i] - r[i+1]) for i in range(n-1)]
print(min(ans))