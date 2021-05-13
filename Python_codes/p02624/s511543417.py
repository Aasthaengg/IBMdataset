N = int(input())

s=k=0;n=N
while k<n:
	k += 1
	n = N//k
	s += k*n*(n+1)
knn = k*n*(n+1)//2
s -= (k+1)*knn//2
if n<k:
	s -= knn

print(s)
