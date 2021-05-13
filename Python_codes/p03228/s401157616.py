A,B,K = map(int,input().split())
turn = "A"
for k in range(K):
    if turn=="A":
        if A%2==0:
            A=A//2
            B+=A
            turn = "B"
        else:
            A=(A-1)//2
            B+=A
            turn="B"
    elif turn=="B":
        if B%2==0:
            B=B//2
            A+=B
            turn="A"
        else:
            B=(B-1)//2
            A+=B
            turn="A"
print(A,B)