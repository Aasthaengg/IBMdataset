n = int(input())
dic = {}
for i in range(n):
  temp = 0
  s = input()
  for j in s:
    temp += (12 ** (ord(j) - ord('a') + 1))
  dic.setdefault(temp, 0)
  dic[temp] += 1
#print(dic)
res = 0
for i in dic:
  if dic[i] >= 2:
    res += ((dic[i] * (dic[i] - 1)) // 2)
print(res)