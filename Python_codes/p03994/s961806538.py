s = list(input())
K = int(input())

"""
Kを使用する
-> aにすることができる

残りのKはs[-1]に使用
"""

from collections import defaultdict
alpha = defaultdict(int)
for i in range(97, 97 + 26):
    alpha[chr(i)] = i - 97

for i in range(len(s)):
    if s[i] == "a":
        continue
    if 26 - alpha[s[i]] <= K:
        K -= 26 - alpha[s[i]]
        s[i] = "a"

if K > 0:
    s[-1] = chr(97 + (alpha[s[-1]] + K) % 26)

print(*s, sep="")