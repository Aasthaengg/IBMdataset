S = input()
print('YES' if max(S.count('a'),S.count('b'),S.count('c'))-min(S.count('a'),S.count('b'),S.count('c')) < 2 else 'NO')
