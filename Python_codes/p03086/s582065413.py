S = input()
i = 0
result = []
for a in S:
  if a == "A" or a == "C" or a == "G" or a == "T":
    i += 1
  else:
    result.append(i)
    i = 0

result.append(i)
result.sort()
print(result[-1])