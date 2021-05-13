K = int(input())
S = str(input())
if len(S) > K:
    S_dash = S[0:K]
    S_dash += '...'
    print(S_dash)
else:
    print(S)