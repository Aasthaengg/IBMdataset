n = int(input())
A = [int(x) for x in input().split()]
dict = {}
res = 0
for i, a in enumerate(A, 1):
  dict[i] = a
for i in range(1, n+1):
  if dict[i] in dict.keys() and dict[dict[i]] == i:
    res += 1
print(res // 2)