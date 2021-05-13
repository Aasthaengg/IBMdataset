N=int(input())
D=[0]*(N+1)
for i in range(2,N+1):
  a=i
  for j in range(2,i+1):
    while a%j==0:
      D[j]+=1
      a//=j
def num(x):
  cnt=0
  for i in D:
    if i>=x-1:
      cnt+=1
  return cnt

print(num(75)+num(25)*(num(3)-1)+num(15)*(num(5)-1)+num(5)*(num(5)-1)*(num(3)-2)//2)
