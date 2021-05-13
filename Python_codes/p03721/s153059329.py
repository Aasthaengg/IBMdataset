n,k = list(map(int,input().strip().split()))

dic= {}
for i in range(n):
  a,b = list(map(int,input().strip().split()))
  if a in dic:
    dic[a] += b
  else:
    dic[a] = b

arr = sorted(dic.items())
leng = 0
for i in arr:
  leng += i[1]
  if leng >= k:
    print(i[0])
    exit()