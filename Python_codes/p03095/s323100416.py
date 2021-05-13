# A - Colorful Subsequence
import numpy as np

N,S = int(input()),input()
count = np.zeros(26)

for i in range(N):
    count[ord(S[i])-ord('a')] += 1

ans = 1
D =10**9+7

for i in range(26):
    ans = int((ans*(count[i]+1))%D)

print(ans-1)