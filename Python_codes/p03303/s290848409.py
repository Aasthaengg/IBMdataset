S = list(input())
w = int(input())

print(''.join([x for x in S[::w]]))
