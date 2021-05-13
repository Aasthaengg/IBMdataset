N=int(input())
S=input()
a=N//2
if S[:a]==S[a:]:
	print('Yes')
else:
	print('No')
