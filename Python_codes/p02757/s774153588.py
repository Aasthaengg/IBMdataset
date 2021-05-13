N, P = input().split()
p_len = len(P)
N = int(N)
P = int(P)

S = input()


cnt = 0
if P in [2,5]:
    for i in range(N):
        cnt += i+1 if int(S[i]) % P == 0 else 0
else:
    table = [0] * P # ?1
    Ui = 0
    ten = 1
    
    S = S[::-1]
    table[0] = 1 # ?2
    
    for i in range(N):
        Ui = (Ui + int(S[i]) * ten) % P # ?3
        
        cnt += table[Ui] # ?4
        
        table[Ui] += 1 # ?5
        ten = (ten * 10) % P # ?6
print(cnt)