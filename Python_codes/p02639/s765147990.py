num = input().split()
i = 0
while  i < 5:
  if int(num[i]) != i + 1:
    print(i+1)
    break
  i += 1