A,B=map(int,input().split())
C=max(A,B)+min(A,B)
if C % 2 !=0:
    print("IMPOSSIBLE")
else:print(C//2)