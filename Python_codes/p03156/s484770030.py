import sys
if sys.platform =='ios':
	sys.stdin=open('input.txt')
	
n = int(input())

a,b = map(int,input().split())

l = list(map(int,input().split()))
k = [0]*3

for i in range(n):
	if l[i]<=a:
		k[0]=k[0]+1
	elif a<l[i]<=b:
		k[1]=k[1]+1
	elif b<l[i]:
		k[2]=k[2]+1

print(min(k))