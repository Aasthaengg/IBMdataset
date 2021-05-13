N = int(input())
A = []
B = []
for i in range(N):
	a,b = map(int,input().split())
	A.append(a)
	B.append(b)
sum = max(A) - min(A) + 1
sum += min(A) - 1
sum += min(B)
print(sum)