T = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

S = [0]*2
for i in range(2):
    S[0] += T[i]*A[i]
    S[1] += T[i]*B[i]
if S[0]==S[1]:
    print("infinity")
else:
    if S[0]<S[1]:
        A,B = B,A
        S = S[::-1]
    if A[0]==B[0] or A[1]==B[1]:
        print(0)
    elif A[0]>B[0] and A[1]>B[1]:
        print(0)
    elif A[0]>B[0] and A[1]<B[1]:
        print(0)
    elif A[0]<B[0] and A[1]>B[1]:
        S = S[0]-S[1]
        T = T[0]*(B[0]-A[0])
        print(T//S*2-1+(1 if T%S==0 else 2))