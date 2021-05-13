T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

if A1 < B1 :
    A1, A2, B1, B2 = B1, B2, A1, A2

def solve() :    
    A = T1 * A1 + T2 * A2
    B = T1 * B1 + T2 * B2
    
    if A == B :
        return 'infinity'
    
    if (A1 > B1 and A > B) or (A1 < B1 and A < B) :
        return 0
    
    D0 = abs(A1 - B1) * T1
    D = abs(A - B)
    
    if D0 % D == 0 :
        return D0 // D * 2
    else :
        return D0 // D * 2 + 1
        
print(solve())
