import sys
n=int(input())
for i in range(1,n+1):
	if(i%3==0 or i%10==3 or '3' in str(i)):
		i=str(i)
		sys.stdout.write(' '+i)
		i=int(i)
print('')