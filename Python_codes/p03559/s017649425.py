def sup(A, j):
	if A[0] >= j:
		return 0
	l = 0
	r = len(A) - 1
	while True:
		i = (l+r) // 2
		if i == len(A) - 1 and A[i] < j:
			return len(A)
		elif A[i]<j and A[i+1]>=j:
			return i+1
		else:
			if A[i] >= j:
				r = i-1
			else: # A[i+1] < j
				l = i+1		

def inf(A, j): 
    if A[-1] <= j:
        return 0
    l = 0
    r = len(A) - 1
    while True:
        i = (l+r) // 2
        if i == 0 and A[i]>j:
            return len(A)
        elif A[i]>j and A[i-1]<=j:
            return len(A)-i
        else:
            if A[i] <= j:
                l = i+1
            else: # A[i-1] > j
                r = i-1		

N = int(input())
[A, B, C] = [sorted([int(i) for i in input().split()]) for j in range(3)]
ans = 0
for j in B:
	ans += sup(A, j) * inf(C, j)
print(ans)