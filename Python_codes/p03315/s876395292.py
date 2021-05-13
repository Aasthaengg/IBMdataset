ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

s = input()

pts = 0
for si in s:
  if si == '+':
    pts+=1
  else:
    pts-=1
print(pts)