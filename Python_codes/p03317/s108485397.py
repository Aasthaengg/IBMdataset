N,K=list(map(int, input().split()))
A=list(map(int, input().split()))
A.pop(1)
f=len(A)//(K-1)
if len(A)%(K-1)==0:
    print(f)
else:
    print(f+1)