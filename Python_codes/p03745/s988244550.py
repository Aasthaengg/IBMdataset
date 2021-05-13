N = int(input())
A = list(map(int,input().split()))
counter = 1 ###グループ数
sign = 0 ###増減、-1,0,1、0はグループの初回、または初回以降増減が見られないときのみ
for x in range (1,N):
	if A[x]>A[x-1] and (sign==0 or sign==1):
		sign = 1
	elif A[x]>A[x-1] and (sign==-1):
		counter += 1
		sign = 0
	elif A[x]<A[x-1] and (sign==0 or sign==-1):
		sign = -1
	elif A[x]<A[x-1] and (sign==1):
		counter += 1
		sign = 0
print(counter)