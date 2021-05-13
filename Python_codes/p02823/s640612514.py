N,A,B=map(int,input().split(' '))
if abs(B-A)%2==0:
    print(abs(B-A)//2)
else:
     l = min(A-1,B-1)+1+(abs(A-B)-1)//2
     r = min(N-A,N-B)+1+(abs(A-B)-1)//2
     print(min(l,r))