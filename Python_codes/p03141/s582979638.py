n=int(input())
s=[]
for i in range(n):
  a,b=map(int,input().split())
  s.append([a+b,a,b])
s=sorted(s,key=lambda x: x[0],reverse=True)
tk,ao=0,0
for i in range(n):
  if i%2==0:
    tk+=s[i][1]
  else:
    ao+=s[i][2]
print(tk-ao)
