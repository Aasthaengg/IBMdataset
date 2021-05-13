S = input()
N = len(S)

L = abs(S.count('0') - S.count('1'))

print(N - L)