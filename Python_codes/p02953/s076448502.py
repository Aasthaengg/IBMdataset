import sys
n=int(input())
hlist=list(map(int,input().split()))

for i in range(1,n):
	if hlist[-i] == hlist[-(i+1)] - 1:
		hlist[-(i+1)] -= 1
	elif hlist[-(i+1)] > hlist[-i]:
		print('No')
		sys.exit()

print("Yes")
