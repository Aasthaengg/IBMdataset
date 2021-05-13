# B - 754
S = list(input())
N = len(S)

lst = []
for i in range(0,N-2):
	ref = abs(753 - int(S[i]+S[i+1]+S[i+2]))
	lst.append(ref)
print(min(lst))
