N = int(input())
S = str(input())
V = 'abcdefghijklmnopqrstuvwxyz'
Lavida = [1]*26
for i in range (0, N):
	Lavida[V.index(S[i])]+=1

count = 1
for i in range (0, 26):
	count*=Lavida[i]
	count=count%(10**9+7)

print((count-1)%(10**9+7))