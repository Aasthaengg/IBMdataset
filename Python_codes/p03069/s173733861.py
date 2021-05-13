n=int(input())
s=input()
w=[0]*(n+1)
b=[0]*(n+1)
for i in range(1,n+1):
  w[i]=w[i-1]+1 if s[i-1]=="#" else w[i-1]
  b[-i-1]=b[-i]+1 if s[-i]=="." else b[-i]
print(min([x+y for x,y in zip(w,b)]))