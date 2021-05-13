N = int(input())
A = list(map(int, input().split(' ')))
denominator = 0
for val in A:
  denominator += 1 / val
res = 1 / denominator
print(res)