S = str(input())

if len(S) == 2:
    print(S)
    
else:
    A = list(reversed(S))
    print(''.join(A))