n = int(input())
d = [int(input()) for i in range(n)]
d_ = [0] * n
c = 0

for i in range(n):
  if d[i] not in d_:
    d_[i] = d[i]
    c += 1
print(c)
