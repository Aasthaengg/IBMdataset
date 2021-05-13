from math import factorial

def combinations_count(n, r):
  return factorial(n) // (factorial(n - r) * factorial(r))

n,p = map(int,input().split())
a = list(map(int,input().split()))

eve = 0
odd = 0

for i in range(n):
	if a[i]%2==0:
		eve += 1
	else:
		odd += 1
		
eve_cb = 2**eve
odd_cb1 = 0
odd_cb2 = 0

if p==1:
  for i in range(1,odd+1)[::2]:
	  odd_cb1 += combinations_count(odd,i)
else:
  for i in range(0,odd+1)[::2]:
	  odd_cb2 += combinations_count(odd,i)

print(eve_cb*(odd_cb1*p + odd_cb2*(1-p)))