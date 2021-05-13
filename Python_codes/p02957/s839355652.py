# ABC 135
A,B =map(int,input().split())

if A%2==B%2:
    print(abs(A+B)//2)
else:
    print("IMPOSSIBLE ")