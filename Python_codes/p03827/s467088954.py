N = int(input())
S = str(input())

count = 0
result = 0
for i in S:
  if i == "I":
    count += 1
  else:
    count += -1
  result = max(count,result)
print(result)