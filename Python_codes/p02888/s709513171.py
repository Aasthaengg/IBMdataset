n = int(input())
a = list(map(int, input().split()))
 
a.sort()
count = 0
for i in range(n-1, 0, -1):
    l = 0
    r = i-1
    while(l<r):
        if a[l] + a[r] > a[i]:
            count += r-l
            r -= 1
 
        else:
            l += 1
 
print(count)