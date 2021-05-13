S = input()

ans = 16

A = 'CODEFESTIVAL2016'

for i in range(16):
    if S[i] == A[i]:
        ans = ans-1
        
print(ans)