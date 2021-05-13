X,A,B=map(int,input().split())
if A>=B:
    print("delicious")
elif A<B and (A+X)>=B:
    print("safe")
else:
    print("dangerous")