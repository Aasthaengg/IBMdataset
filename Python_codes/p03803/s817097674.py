A,B=map(int,input().split())
if A==1:
    A=14
if B==1:
    B=14
if A==B:
    print("Draw")
if A>B:
    print("Alice")
if B>A:
    print("Bob")