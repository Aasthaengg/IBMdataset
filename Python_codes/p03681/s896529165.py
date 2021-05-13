n, m = map(int , input().split())
ans  = 1
mod = 10**9+7
for i in range(1, n+1):
	ans = (ans%mod)*(i%mod)
	ans = ans%mod
for i in range(1, m+1):
	ans = (ans%mod)*(i%mod)
	ans = ans%mod
# if the difference between them is greater than 1 they can't be arranged
if abs(n-m)>1:
	print(0)
# if they have same number they can be placed in odd position or even position independently
elif abs(n-m)==0:
	ans = ans*2
	ans = ans%mod
	print(ans)
# only one way no exchange of odd and even place 
else:
	print(ans)