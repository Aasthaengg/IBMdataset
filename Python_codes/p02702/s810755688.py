# D - Multiple of 2019
S = input()
mod = [1]+[0]*2018
tmp = 0
seki = 1
for k in range(len(S)):
    tmp = (seki*int(S[len(S)-1-k])+tmp)%2019
    mod[tmp] += 1
    seki = (seki*10)%2019
ans = 0
for k in range(2019):
    ans += mod[k]*(mod[k]-1)//2
print(ans)