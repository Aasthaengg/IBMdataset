N = int(input())
A = list(map(int, input().split()))
sort_A = sorted(A)
str_A = list(map(str, sort_A))
o = 'YES'
for i in range(1, len(A)):
	if str_A[i-1] == str_A[i]:
		o = 'NO'
		break
print(o)