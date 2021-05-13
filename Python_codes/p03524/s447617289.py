S = input()
C = [S.count('a'), S.count('b'), S.count('c')]
if (len(set(list(S))) == 3 and max(C) - min(C) < 2) or len(S) == 1 or (len(S) == len(set(list(S))) == 2):
    print('YES')
else:
    print('NO')