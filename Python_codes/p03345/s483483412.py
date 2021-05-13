A,B,C,K = map(int,input().split())

if K % 2 == 0:
	print(A-B) if abs(A-B)<=10**18 else print("Unfair")
else:
	print(B-A) if abs(A-B)<=10**18 else print("Unfair")
