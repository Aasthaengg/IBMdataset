n,k = map(int,input().split())
a = list(map(int,input().split()))
dict = {}
sum = 0

for i in a:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] += 1

kind = len(dict)-k
if kind <=0:
  print(0)
  exit()

dic= sorted(dict.items(), key=lambda x:x[1])

for i in range(kind):
  sum += dic[i][1]
  
print(sum)