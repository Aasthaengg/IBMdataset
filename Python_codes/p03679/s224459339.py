X,A,B = map(int,input().split())

a = B - A
if a<=0:
    print("delicious")
elif a>=(X+1):
    print("dangerous")
else:
    print("safe")