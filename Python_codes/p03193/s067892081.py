n, h, w = list(map(int, input().split()))
count=0
for _ in range(n):
  _h, _w = list(map(int, input().split()))
  count += (int(_h/h) * int(_w/w))>0

print(count)