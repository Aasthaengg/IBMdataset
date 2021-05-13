n,m=map(int, raw_input().split())
x=map(int, raw_input().split())
y=map(int, raw_input().split())

x1=[]
x_sum=0
for i in range(n):
	x_sum+=( (n-i-1)-i )*x[i]

y_sum=0
for i in range(m):
	y_sum+=( (m-i-1)-i )*y[i]


print x_sum*y_sum%(10**9+7)