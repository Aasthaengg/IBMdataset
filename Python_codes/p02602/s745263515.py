n, k = map(int, input().split())
A = list(map(int, input().split()))
point = 0
for i in range(k):
    point += A[i]
for i in range(k,n):
    x = point-A[i-k]+A[i]
    if point < x: print("Yes")
    else: print("No")
    point = x