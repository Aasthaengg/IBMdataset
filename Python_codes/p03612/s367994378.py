n=int(input())
A=list(map(int,input().split()))+[0]
c=0
for i in range(n):
  j=i+1
  a=A[i]
  if a==j:
    c+=1
    A[i]=A[i+1]
    A[i+1]=j
print(c)