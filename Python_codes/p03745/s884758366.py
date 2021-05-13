n = int(input())
a = list(map(int, input().split()))
cnt = 1
b = [0] + a
c = [(i-j)//abs(i-j) for i, j in zip(a, b) if i != j]
del c[0]
if c:
  mae=c[0]
  d=iter(c)
  for x in d:
    if x != mae:
      cnt += 1
      try:
        mae = d.__next__()
      except StopIteration:
        break
print(cnt)