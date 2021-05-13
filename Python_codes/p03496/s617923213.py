n = int(input())
a = list(map(int,input().split()))

min1 = min(a)
max1 = max(a)
idx1 = a.index(min1)
idx2 = a.index(max1)

print(2*n-2)

if abs(min1) < abs(max1):
    for i in range(n):
        if i != idx2:
            print(idx2+1, i+1)
    for i in range(n-1):
        print(i+1, i+2)

else:
    for i in range(n):
        if i != idx1:
            print(idx1+1, i+1)
    for i in range(n-1):
        print(n-i, n-i-1)
