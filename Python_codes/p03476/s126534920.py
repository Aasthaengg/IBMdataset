def is_prime(N):
    if N == 1: return False
    if N == 2: return True
    
    d = 2 
    while d*d <= N:
        if N % d == 0: return False
        d += 1
    return True

Q = int(input())

S = [0]*100010
for i in range(3,100010,2):
    S[i] += S[i-2]
    if is_prime(i) and is_prime((i+1)//2):
        S[i] += 1

for q in range(Q):
    l, r = map(int,input().split())
    print(S[r] - S[max(0,l-2)])
