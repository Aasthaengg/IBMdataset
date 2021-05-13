A,B,C = list(map(int,input().split()))
if abs(A-B) < abs(A-C):
    print("A")
else:
    print("B")