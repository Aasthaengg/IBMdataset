n, m, d = list(map(int, input().split()))
a = 0 if d == 0 else max(0, n-2*d)/n
print((1+a)*(m-1)/n)