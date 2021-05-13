n, l = map(int, input().split())
a = [l + i for i in range(n)]
s = 1 if sum(a) >= 0 else -1 
print(sum(a) - s * min(abs(a[i]) for i in range(n)))