n=int(input())
a=[]
for i in range(1,n):
  s=str(i)+str(n-i)
  c=0
  for j in s:
    c+=int(j)
  a.append(c)
    
print(min(a))