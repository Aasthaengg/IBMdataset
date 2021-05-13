K = int(input())
S = str(input())

n = len(S)
list_S = list(S)

if n > K:
    tmp = list_S[0:K]
    print(''.join(tmp) + '...')
else:print(''.join(list_S))