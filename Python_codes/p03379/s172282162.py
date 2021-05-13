ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
x=nl()

sx = sorted(x)[::-1]

c = n//2

for i in range(n):
  if x[i] > sx[c]:
    print(sx[c])
  else:
    print(sx[c-1])
