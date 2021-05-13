k=int(input())
a,b=map(int, input().split())
ok=False
for i in range(a, b+1):
  ok = ok or (i % k == 0)
print(['NG','OK'][ok])