import math
t = 1
for tc in range(t):
    S = input()
    n = len(S)
    if S[n-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')

    
    
