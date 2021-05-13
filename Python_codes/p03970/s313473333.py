S = input()
T = 'CODEFESTIVAL2016'

print(sum(S[i] != T[i]for i in range(16)))