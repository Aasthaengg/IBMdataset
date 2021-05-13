S = list(input())
N = len(S)
T = input()
S += S
A = [''.join(S[i:i+N]) for i in range(N)]
if T in A:
    print('Yes')
else:
    print('No')