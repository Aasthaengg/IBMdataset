S,T = (input() for T in range(2))
ReS = ''.join(sorted(S))
ReT = ''.join(sorted(T)[::-1])
if ReS<ReT:
    print('Yes')
else:
    print('No')