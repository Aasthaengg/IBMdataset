n,k=[int(x) for x in input().rstrip().split()]
dic={}
for i in range(n):
  a,b=[int(x) for x in input().rstrip().split()]
  if a not in dic:
    dic[a]=b
  else:
    dic[a]+=b

dic=sorted(dic.items())

now=0
for i,v in dic:
  now+=v
  if k<=now:
    print(i)
    break
