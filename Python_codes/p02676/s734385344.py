N = int(input())
S = str(input())

if len(S) > N:
    print(S[:N] + '...')
else:
    print(S)