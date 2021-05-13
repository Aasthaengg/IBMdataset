n,k=map(int,input().split())
x=k-n+1
out=""
for i in range(2*(n-1)+1):
  out+=str(x+i)+" "
print(out[:-1])
