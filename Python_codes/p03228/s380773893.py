A,B,K=map(int,input().split())


k=0
for i in range(100):
    if A%2==1:
        A-=1
    B=B+A//2
    A=A-A//2
    k+=1
    if k== K:
        print(A,B)
        break
    if B%2==1:
        B-=1
    A=A+B//2
    B=B-B//2
    k+=1
    if k== K:
        print(A,B)
        break