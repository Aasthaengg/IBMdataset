a,b,c,d=map(int,input().split())
if abs(a-b)>100000000000000000:
	print("Unfair")
elif d%2==0 and abs(a-b)<=1000000000000000000:
    print(a-b)
else:
    print(b-a)