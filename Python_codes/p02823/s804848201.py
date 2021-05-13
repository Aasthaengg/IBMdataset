N,A,B = map(int,input().split())
if abs(B-A)%2==0:
    print(abs(B-A)//2)
elif A<B:
    print(min(A-1,N-B)+1+(B-A-1)//2)
else:
    print(min(B-1,N-A)+1+(A-B-1)//2)