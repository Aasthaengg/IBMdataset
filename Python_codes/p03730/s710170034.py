import sys
a,b,c = map(int,input().split())
for i in range(1,1001):
	if (a*i)%b == c:
		print("YES")
		sys.exit()
print("NO")