a,b,k=map(int,input().split())
out=[]
for i in range(k):
  if a+i>=b-i:
    if a+i==b-i:
      out.append(a+i)
    break
  out.append(a+i)
  out.append(b-i)
out.sort()
for i in out:
  print(i)