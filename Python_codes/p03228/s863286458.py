A,B,K = map(int,input().split())
for i in range(K):
    if A%2 == 1:
        A-=1
    B = A//2+B
    A = A//2
    A,B = B,A
if K%2==0 :
    print(A,B)
else :
    print(B,A)
