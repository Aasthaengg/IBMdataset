n = int(input())
k = int(input())
now = 1
def a(n): return n * 2
def b(n): return n + k
for _ in range(n):
    now = min(a(now), b(now))
print(now)