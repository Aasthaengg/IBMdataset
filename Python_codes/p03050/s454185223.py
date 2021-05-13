import math
n = int(input())
a = math.sqrt(n)
if int(a)<a:
  a=int(a)+1
else:
  a=int(a)
ans = 0
for i in range(1,a):
  if (n-i)%i==0 and n%((n-i)//i)==i:
    ans+=(n-i)//i
print(ans)