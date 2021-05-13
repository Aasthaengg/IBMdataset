N,A,B,C,D=map(int,input().split())
S=input()
if '##' in S[A-1:C] or '##' in S[B-1:D]:
    print('No')
    exit()

if C<D:
    print('Yes')
else:
    cnt=0
    for i in range(B-1,D):
        if S[i-1]==S[i] and S[i]==S[i+1] and S[i]=='.':
            print('Yes')
            exit()
    print('No')