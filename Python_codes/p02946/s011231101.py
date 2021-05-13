k, x = map(int, input().split())
lst = list(range(x - (k - 1), x + k))
str1 = ''
for i in range(len(lst)):
  if -1000000 <= lst[i] <= 1000000:
    str1 = str1 + str(lst[i]) + ' '
print(str1[:-1])