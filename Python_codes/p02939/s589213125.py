S = list(input())
N = len(S)
old = S[0]
T = ''
ans = 1
for i in range(1, N):
    if T == '':
        T = S[i]
        if T != old:
            ans += 1
            old = T
            T = ''        
    else:
        T += S[i]
        old = T
        ans += 1 
        T = ''
print(ans)