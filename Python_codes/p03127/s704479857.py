
n=int(input())
a_=list(map(int,input().split()))

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
  
m=a_[0]
for i in range(n):
  m=gcd(m,a_[i])
  
print(m)
