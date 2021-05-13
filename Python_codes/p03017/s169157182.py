N,A,B,C,D = map(int,input().split())
S = input()
if '##' in S[A:C]:
    print('No')
elif '##' in S[B:D]:
    print('No')
elif C>D:
    #print(S[B - 2:D + 1])
    if not '...' in S[B-2:D+1]:
        print('No')
    else:
        print('Yes')
else:
    print('Yes')
