import sys
if sys.platform =='ios':
	sys.stdin=open('input.txt')
	
x,y = map(int,input().split())

if x==1 and y==1:
	print(1000000)
	exit()
	
ans = 0

if x==1:
	ans = ans + 300000
elif x==2:
	ans = ans + 200000
elif x==3:
	ans = ans + 100000

if y==1:
	ans = ans + 300000
elif y==2:
	ans = ans + 200000
elif y==3:
	ans = ans + 100000

print(ans)
