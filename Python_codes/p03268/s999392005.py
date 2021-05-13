n, k = map(int, input().split())

s = n // k
a = n % k
h = 0

if k % 2 == 0 and a >= k/2:
    h = s+1
elif k % 2 == 0:
    h = s

print(s**3 + h**3)
