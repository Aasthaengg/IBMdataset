A,B,C,K=map(int,input().split())
if A>=K:
	print(K)
elif A+B>=K and A<K:
	print(A)
elif A+B+C>=K and A+B<K:
	print(A-1*(K-A-B))