n, k = map(int, input().split())
s = 0
if k % 2 == 0:
    x = [i for i in range(1, n+1) if i % k == k//2]
    s += len(x)**3
y = [i for i in range(1, n+1) if i % k == 0]
s += len(y)**3
print(s)