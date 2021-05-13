n,m=map(int,input().split())
a=[]
for i in range(n):
  ai=list(input())
  a.append(ai)
b=[]
for i in range(m):
  bi=list(input())
  b.append(bi)

frag='No'
for i in range(n-m+1):
  for j in range(n-m+1):
    for k in range(m):
      if a[i+k][j:j+m]!=b[k]:
        break
    else:
      frag="Yes"
      break
  continue
print(frag)