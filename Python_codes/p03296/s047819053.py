n = int(input())
slime = [int(x) for x in input().split()]
border = [0] + [i+1 for i in range(n-1) if slime[i] != slime[i+1]]

if len(border):
  border.append(n)
  count = sum([(border[i+1] - border[i]) // 2 for i in range(len(border) - 1)])
else:
  count = n // 2

print(count)