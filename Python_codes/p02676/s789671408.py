K = int(input())
S = input()
len_S = len(S)
S0 = ''
if len_S<=K:
    print(S)
else:
    S0 += S[0:K]
    S0 +='...'
    print(S0)