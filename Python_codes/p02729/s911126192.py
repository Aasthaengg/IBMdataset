import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N,M=map(int,input().split())
if N==0 or N==1:
    if M==0 or M==1:
        print(0)
        exit(0)
    else:
        print(combinations_count(M, 2))
        exit(0
        )
if M==0 or M==1:
    if N==0 or N==1:
        print(0)
        exit(0)
    else:
        print(combinations_count(N, 2))
        exit(0)
        

print(combinations_count(N, 2)+combinations_count(M, 2))