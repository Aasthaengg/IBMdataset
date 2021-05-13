ls = list(input())
lt = list(input())
count = 0
for i in range(len(ls)):
  if ls[i] == lt[i]:
    count += 1
print(count)