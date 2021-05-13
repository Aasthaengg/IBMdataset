s = input()
k = int(input())
n = len(s)

S = list(s)

import string
A = [chr(i) for i in range(ord("a"), ord("z")+1)]
B = {}
for i in range(26):
    B[A[i]] = i

for i in range(n):
    if S[i] != "a" and 26 - B[S[i]] <= k:
        k -= 26 - B[S[i]]
        S[i] = "a"
        
# print(k)
if k > 0:
    S[-1] = A[(B[S[-1]] + k) % 26]

# print(S)

print("".join(S))