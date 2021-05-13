S = input()
odd_S = S[0::2]
even_S = S[1::2]
if 'L' in odd_S or 'R' in even_S:
    print('No')
else:
    print('Yes')
    
