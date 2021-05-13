s = input()

pivot = s[0]
result = 0
for c in s:
  if pivot != c:
    pivot = c
    result += 1
print(result)