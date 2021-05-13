a=int(input())
n=2*(a//11)+(a%11//7)+1
if a%11==0:
  n-=1
print(n)
