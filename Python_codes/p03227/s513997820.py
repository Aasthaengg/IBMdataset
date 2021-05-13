S = input()
T = ''
if len(S) == 2:
    T = S
else:
    T = S[2] + S[1] + S[0]
print(T)