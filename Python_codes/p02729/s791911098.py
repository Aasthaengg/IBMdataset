import math

N,M = map(int,input().split())
#Nは偶数
#Mは奇数

#偶数偶数
if N >= 2:
  Nf = math.factorial(N)//(math.factorial(N-2)*2)
else:
  Nf = 0
#奇数奇数
if M >= 2:
  Mf = math.factorial(M)//(math.factorial(M-2)*2)
else:
  Mf = 0
ans = int(Nf + Mf)
print(ans)
