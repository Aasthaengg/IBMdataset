s = input()

min_value = 10 ** 9

# 左端に置く場合
pivot = s[0]
result = 0
for c in s:
  if pivot != c:
    pivot = c
    result += 1
min_value = min(min_value, result)

# 右端に置く場合
result = 0
for c in reversed(s):
  if pivot != c:
    pivot = c
    result += 1
min_value = min(min_value, result)
print(min_value)