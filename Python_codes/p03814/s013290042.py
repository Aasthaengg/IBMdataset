S = input()
s = S.index('A')
e = [i for i, x in enumerate(S) if x == 'Z']

print(max(e) - s + 1)