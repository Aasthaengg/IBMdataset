import math
A, B, C, D = map(int, input().split())

def LCM(S, T):
    return (S*T)//math.gcd(S, T)

def f(N, S, T):#Nを含む
    return N- N//S - N//T + N//LCM(S, T)
    
    
print(f(B, C, D)-f(A-1, C, D))