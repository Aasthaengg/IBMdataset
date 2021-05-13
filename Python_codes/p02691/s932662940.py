n = int(input())
lst = [int(i) for i in input().split()]

dic = {}
count = 0
for i in range(n):
  num = lst[i]
  a = i + num
  if a not in dic:
    dic[a] = 1
  else:
    dic[a] += 1
  b = i - num
  if b in dic:
    count += dic[b]
print(count)