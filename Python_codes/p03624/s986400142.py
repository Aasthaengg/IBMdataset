S = input()
N = len(S)

X = set()
ans = 'None'

for i in range(N):
    X.add(S[i])

for alph in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',\
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
         'w', 'x', 'y', 'z']:
         if alph not in X:
             ans = alph
             break

print(ans)