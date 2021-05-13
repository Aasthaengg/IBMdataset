from collections import Counter
N=int(input())
S = input()
ss = list(Counter(S).most_common())
#print(ss)
ans = 1
MOD = 10**9 + 7
for i in range(len(ss)):
    ans *= ss[i][1] +1
    ans %= MOD
print(ans-1)