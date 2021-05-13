A, B, C = map(int,input().split())
if(A+B+1 >= C):
    print(str(B+C))
else:
    print(str(A+B+1+B))