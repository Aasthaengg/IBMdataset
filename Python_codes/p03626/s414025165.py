N = int(input())
S1 = list(input())
S2 = list(input())

mod = 1000000007

if S1[0] == S2[0]:
    ans = 3
    c = 1
else:
    ans = 6
    c = 2
    
i = c
while i < N:
    if S1[i] == S2[i]:
        ans *= (3-c)
        ans %= mod
        c = 1
        i += 1
    elif c == 1:
        ans *= 2
        ans %= mod
        c = 2
        i += 2
    else:
        ans *= 3
        ans %= mod
        c = 2
        i += 2
        
print(ans)