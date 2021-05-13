N = int(input())
S = input()

one = S[:N//2]
two = S[N//2:]

if one == two:
    print('Yes')
else:
    print('No')
