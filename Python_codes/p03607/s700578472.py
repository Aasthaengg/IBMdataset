n = int(input())

dic = {}
for i in range(n):
  a = int(input())
  if not a in dic:
    dic[a] = 1
  else:
    dic[a] += 1
print(len([k for k, v in dic.items() if v % 2 != 0]))