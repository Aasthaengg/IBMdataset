# A - Diverse Word
import numpy as np

S = input()
alphabet = np.zeros(26, dtype=int)
for i in S:
    alphabet[ord(i)-97]=1
if len(S)<26:
    add = alphabet.argmin()
    ans = S + chr(add+97)
else:
    i = 24
    while(i>=0 and S[i]>S[i+1]):
        i -= 1
    if i==-1:
        ans = '-1'
    else:
        j = 25
        while(i+1<j and S[i]>S[j]):
            j -= 1
        ans = S[:i] + S[j]

print(ans)