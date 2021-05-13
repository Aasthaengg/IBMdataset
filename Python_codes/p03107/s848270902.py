S = input()

N = len(S)
O = S.count('1')
Z = N - O

print(2*min(O,Z))