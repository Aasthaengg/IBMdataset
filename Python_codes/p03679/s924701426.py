X,A,B=(int(n) for n in input().split())
if A>=B:
    print("delicious")
elif (A<B) and (B-A<=X):
    print("safe")
else:
    print("dangerous")