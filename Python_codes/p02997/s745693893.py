import os, sys, re, math, queue

N,K = list(map(int,input().split(' ')))
ans = []

if (N-1)*(N-2) < 2*K:
	print('-1')
	sys.exit()

for i in range(2,N+1):
	ans.append('1 ' + str(i))

for i in range(2, N):
	for j in range(i+1, N+1):
		ans.append(str(i) + ' ' + str(j))

limit = N - 1 + (N-1)*(N-2)//2 - K
print(limit)
for k in range(limit):
	print(ans[k])
