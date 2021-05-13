K,A,B=map(int,input().split())
if A<B:
	if K+2<A:
		print(K+1)
	else:
		T=K-(A-1)
		if T%2==0:
			ans=A+(T//2)*(B-A)
			print(max(ans,K+1))
		else:
			ans=A+(T//2)*(B-A)
			print(max(ans+1,K+1))
else:
	print(K+1)