N = int(input())
dic = {}
for i in range(1, N+1):
  n = i 
  cnt = 0
  while i % 2 == 0:
    cnt += 1
    i = i // 2
  dic[n] = cnt

a = 0
b = 0
for k, v in dic.items():
  if a < v:
    b = k
    a = v

if b == 0:
  print(1)
else:
  print(b)
