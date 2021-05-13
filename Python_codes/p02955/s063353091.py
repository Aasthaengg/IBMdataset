# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left, bisect_right

N,K=map(int, sys.stdin.readline().split())
A=map(int, sys.stdin.readline().split())

s=sum(A)
n=int(s**0.5)

#約数のリスト
cd=[]

for i in range(1,n+2):
	if s%i==0:
		cd.append(i)
		cd.append(s/i)

cd.sort(reverse=True)

def check(t):
	if t==1: return True
	A_temp=[]
	for x in A:
		A_temp.append(x%t)

	A_temp.sort()

	#Aの配列をmod tした配列A_tempの累積和
	A_temp_sum=[]

	for i,x in enumerate(A_temp):
		if i==0: A_temp_sum.append(x)
		else: A_temp_sum.append(A_temp_sum[-1]+x)

	#配列の前半は、数字をマイナスしていく
	p1=min(bisect_left(A_temp_sum,K),N-2)
	if A_temp_sum[p1]<=K:
		k1=A_temp_sum[p1]
	else:
		#配列の項数p1の値がKを超えている場合は、p1の1個手前の値をとる
		p1-=1
		k1=A_temp_sum[p1]


	#配列の後半で、数字をどれだけプラスする必要があるか
	k2=t*(N-p1-1)-(A_temp_sum[-1]-A_temp_sum[p1])

	#プラスする量が、マイナスする量より少なければ成立
	if k2<=k1:
		return True
	else:
		return False

for x in cd:
	if check(x):
		print x
		quit()
