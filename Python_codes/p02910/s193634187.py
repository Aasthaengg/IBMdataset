import sys
S = list(input())
S_odd = S[::2]
S_even = S[1::2]
easy_odd = ['R','U','D']
easy_even = ['L','U','D']

print('Yes') if set(S_odd).issubset(easy_odd) and set(S_even).issubset(easy_even) else print('No')