S = input()

if len(S) == 3:
    S = list(S)
    S.reverse()
    S = ''.join(S)

print(S)
