n, k, q = map(int, input().split())
a = [int(input()) for i in range(q)]
l = [k-q] * n
for i in a:
  l[i-1] += 1
for f in l:
  if f <= 0:
    print("No")
  else:
    print("Yes")