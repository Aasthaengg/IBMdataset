S = list(input())
cn = 0
T = S[::-1]


for i in range(len(S)//2):
    if S[i] != T[i]:
        cn = cn + 1

print(cn)