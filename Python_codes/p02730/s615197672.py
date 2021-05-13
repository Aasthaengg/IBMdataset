S = input()

N = len(S)//2

print('Yes' if S[:N] == S[-N:] else 'No')