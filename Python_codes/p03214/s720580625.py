n = int(input())
lst = list(map(int, input().split()))
m = sum(lst) / n
z = 10 ** 20
for i in range(n):
  a = abs(lst[i] - m)
  if a < z:
    z = a
    idx = i
print(idx)