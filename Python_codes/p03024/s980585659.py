S = input()
print('YES' if 7-len(S)>=-sum([c=='o' for c in S]) else 'NO')