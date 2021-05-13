n = int(input())
p=1
def cal(a,b):
  return a*b%1000000007

for i in range(1,n+1):
  p = cal(p,i)
  
print(p)