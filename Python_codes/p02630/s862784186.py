n = int(input())
lst = [int(i) for i in input().split()]
dic = {}
for i in range(n):
  key = lst[i]
  if key not in dic:
    dic[key] = 0
  dic[key] += 1
#print(dic)
sum = 0
for key, value in dic.items():
  sum += key * value

m = int(input())
for _ in range(m):
  lst_s = list(map(int, input().split()))
  number = dic.get(lst_s[0])
  if number is not None:
    if lst_s[1] in dic:
      dic[lst_s[1]] += number
    else:
      dic[lst_s[1]] = number
    sum += lst_s[1] * number
    sum -= lst_s[0] * number
    dic.pop(lst_s[0])
  print(sum)