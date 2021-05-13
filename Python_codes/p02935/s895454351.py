n = int(input())
lst = sorted(list(map(int, input().split())))
for i in range(n - 1):
  lst[i + 1] = (lst[i + 1] + lst[i]) / 2
print(lst[-1])