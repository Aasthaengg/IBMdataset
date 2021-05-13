N = int(input())
S = list(input())


cn = 0

for i in range(N-2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        cn = cn + 1
        
        
print(cn)