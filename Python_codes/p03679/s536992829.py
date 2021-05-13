X,A,B = map(int,input().split())	
if A-B>=0:
    print("delicious")
elif B-A<=X:
    print("safe")
elif B-A>X:
    print("dangerous")