ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a=nl()
k=ni()

for i in range(k):
  a = sorted(a)[::-1]
  a[0]*=2

print(sum(a))