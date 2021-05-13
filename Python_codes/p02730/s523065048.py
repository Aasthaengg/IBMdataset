S = input()
m = len(list(S)) // 2
l = m + 1
print('Yes' if (S == S[::-1]) & (S[:m] == S[:m:][::-1]) & (S[l:] == S[l::][::-1]) else 'No')
