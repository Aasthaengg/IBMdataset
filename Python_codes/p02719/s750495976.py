n, k = map(int,input().split())
x1 = n%k
x2 = k - x1
print(min(x1, x2))
