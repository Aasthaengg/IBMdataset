N = input()

num = {}
for a in map(int, input().split()):
  if not a in num.keys(): num[a] = 1
  else: num[a] += 1

res = 0
for a, a_num in num.items():
  if a_num < a: res += a_num
  else: res += a_num - a
print(res)