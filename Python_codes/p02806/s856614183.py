n=int(input())
dic={}
sl=[]
for i in range(n):
  s,t=map(str,input().split())
  dic[s]=int(t)
  sl.append(s)
x=input()

ans=0
flag=False
for s in sl:
  if flag:
    ans+=dic[s]
  if s==x:
    flag=True
print(ans)