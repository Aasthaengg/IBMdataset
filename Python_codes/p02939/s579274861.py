import math
S = input()
ans = 0
i = 0
while i < len(S):
    c = 1
    while i < len(S) -1 and S[i] == S[i+1]:
        c += 1
        i += 1
    if c % 3 == 2 and i < len(S) -1:
        c += 1
        i += 1
    ans += ( c // 3 ) * 2 + math.ceil( c % 3 / 3 )
    i += 1
print(ans)
