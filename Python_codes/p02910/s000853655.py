S = input()
odd = S[::2]
even = S[1::2]
if not('L' in odd) and not('R' in even):
    print('Yes')
else:
    print('No')