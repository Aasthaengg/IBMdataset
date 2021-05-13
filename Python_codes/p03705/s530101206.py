N,A,B = map(int,input().split())
if A>B:
    print(0)
elif N==1 and A<B:
    print(0)
else:
    totmin = A*(N-1)+B
    totmax = A+B*(N-1)
    print(totmax-totmin+1)