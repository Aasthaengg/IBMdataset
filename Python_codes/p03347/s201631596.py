n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))
a.reverse()

f=True
t=0
c=0
for i in a:
  if i==t:
    t-=1
  elif i<t:
    f=False
    break
  else:
    t=i-1
    c+=i
if t!=-1:
  f=False
print(c if f else -1)