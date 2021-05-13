A= list(input())
while True:
    A.pop()
    A.pop()
    B=len(A)//2
    if A[:B]==A[B:]:
        print(len(A))
        break