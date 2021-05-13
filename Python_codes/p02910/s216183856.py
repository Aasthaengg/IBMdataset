S = input()
S_even = S[1::2]
S_odd = S[0::2]

if 'L' not in S_odd and 'R' not in S_even:
    print('Yes')
else:
    print('No')
