#n = int(input())
#n,k = map(int,input().split())
#x = list(map(int,input().split()))

import string

N = int(input())
S = list(input())

cnt = [0 for i in range(26)]

for i in range(N):
    mm = ord(S[i])-97
    cnt[mm] += 1

mod = 10**9+7
ans = 1
for i in range(26):
    ans *= cnt[i]+1
    ans %= mod
print(ans-1)

