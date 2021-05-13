import itertools
x = int(input())
a = x // 100
b = x - a * 100
arr = [0, 1, 2, 3, 4, 5]
ans = 0
for v in itertools.combinations_with_replacement(arr, a):
    k = sum(list(v))
    if k == b:
      ans = 1
      break
print(ans)