A,B=map(str,input().split())
X,Y=map(int,input().split())
C=input()

if A==C:
    print(X-1,Y)
else:
    print(X,Y-1)