a,b,c,d = map(int,input().split())
A,B = a+b,c+d
if A > B:
    print("Left")
elif A < B:
    print("Right")
else:
    print("Balanced")