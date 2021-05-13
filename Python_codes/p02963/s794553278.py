S=int(input())
M=10**9
Q,R=divmod(S,M)

if R:
    print(0,0,M,1,M-R,Q+1)
else:
    print(0,0,M,1,0,Q)