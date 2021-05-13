A,B,C=map(int,input().split())

if B-A*C>=0:
    print(C)
else:
    print(int(B/A))