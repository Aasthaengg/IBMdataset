A,P = map(int,input().split())
if A % 2 == 1 and P % 2 == 1:
    print(A*3//2+(P//2)+1)
else:
    print(A*3//2+(P//2))    