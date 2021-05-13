import sys
input=sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))
l=0
for i in range(1,N):
	if abs(a[i])>abs(a[l]): l=i

if a[l]==0: print(0),sys.exit()
elif a[l]>0:
	print(N*2)
	for i in range(2):
		print(l+1,1)
	for i in range(1,N):
		for j in range(2):
			print(i,i+1)

else:
	print(N*2)
	for i in range(2):
		print(l+1,N)
	for i in range(N,1,-1):
		for j in range(2):
			print(i,i-1)