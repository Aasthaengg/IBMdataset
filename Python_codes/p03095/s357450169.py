from collections import Counter
N = int(input())
S = list(input())
mod = pow(10, 9)+7
X = Counter(S)
ans = 1
for i in X.values():
    ans = (ans*(i+1)) % mod
print(ans-1)
