S = input()
N = len(S) 
ans = 0
for i in range(2**(N-1)):
    f = S[0]
    for j in range(N-1):
        if ( i >> j ) & 1 :
            f += '+'
        f += S[j+1]
    ans += sum(map(int,f.split('+')))
print(ans)