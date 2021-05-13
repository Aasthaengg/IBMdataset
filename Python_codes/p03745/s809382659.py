n = int(input())
a = list(map(int, input().split()))

i = 0
ans = 0

while i < n:
    i1 = i
    last = a[i]
    while i1 < n:
        if last <= a[i1]:
            last = a[i1]
            i1 += 1
        else: break
    
    i2 = i
    while i2 < n:
        if last >= a[i2]:
            last = a[i2]
            i2 += 1
        else: break
    
    i = max(i1, i2)
    ans += 1

print(ans)