a,b,c = map(int,input().split())
cnt = 0
def f(a,b,c):
	return b//2 + c//2, a//2 + c//2, a//2 + b//2

while (a%2==0 and b%2==0 and c%2==0):
	if a==b and b==c and c==a:
		print('-1')
		exit()
	else:
		cnt += 1
		a,b,c = f(a,b,c)
print(cnt)