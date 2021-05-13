n=int(input())
dic={}
count={}

for i in range(n):
  s,p=map(str,input().split()) 
  p=int(p)
  dic[p]=s
  count[p]=i+1
  
a=sorted(dic.items(),reverse=True)
a=sorted(a,key=lambda x:x[1])

for p,s in a:
  for q,i in count.items():
    if p==q:
      print(i)