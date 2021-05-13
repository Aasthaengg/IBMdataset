n=int(input())
a=[int(x) for x in input().rstrip().split()]
dic={}
minus=0
for i in a:
  if i not in dic:
    dic[i]=1
  else:
    dic[i]+=1

for i in dic:
  v=dic[i]
  if i==v:
    continue
  elif i<v:
    minus+=v-i
  else:
    minus+=v

print(minus)