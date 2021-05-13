S = list(input())
s = len(S)-1
from itertools import product
a = list(product(["+",""],repeat=s))
ans = 0
for i in a:
    b = ""
    for j in range(len(S)):
        if j<=s-1:
            b += S[j]
            b += i[j]
        else:
            b += S[j]
    ans += eval(b)
print(ans)