s=input()
k=int(input())
l=[]
n=len(s)

for i in range(n):
  if n+1>=i+6:
    l+=[s[i:j] for j in range(i+1,i+6)]
  else:
    l+=[s[i:j] for j in range(i+1,n+1)]

l=sorted(list(set(l)))
print(l[k-1])