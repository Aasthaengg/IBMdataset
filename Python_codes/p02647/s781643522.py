n , k = map(int,input().split())
a = list(map(int,input().split()))
for j in range(k):
    b = [0 for i in range(n)]
    for i in range(n):
        b[max(0,i-a[i])] += 1
        if i+a[i]+1 < n:
            b[i+a[i]+1] -= 1
    for i in range(n-1):
        b[i+1] += b[i]
    if a == b:
        print(*b)
        exit()
    a = b[:]
print(*b)