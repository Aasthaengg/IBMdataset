import math
from fractions import Fraction

#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

n,k=input2()
ans=0
for i in range(1,n+1):
	point=i
	if point>=k:
		ans+=Fraction(n-point+1,n)
		break
	else:
		tmp=math.ceil(math.log2((k/point)))
		ans+=Fraction(1,n)*Fraction(1,2**tmp)
print(float(ans))