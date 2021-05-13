inp = input
out = print
N, K = map(int, inp().split())
S = inp().rstrip('\n')

S += '1' if S[N-1] == '0' else '0'

#count
lenz = []
valz = []
cnt = 1
for i in range(1, N+1):
    if S[i] == S[i-1]:
        cnt += 1
    else:
        #add to lenz
        lenz.append(cnt)
        valz.append(1 if S[i-1] == '1' else 0)
        cnt = 1

M = len(lenz)
sumz = 0#[0]*(M+1)
maxsum = 0
right = 0
cnt = 0
left = 0
while left < M:
    while right < M:
        if valz[right] == 0:
            cnt += 1
        if cnt > K: break
        sumz += lenz[right]
        right += 1
    if maxsum < sumz: maxsum = sumz

    if right >= M:
        #finish, no more longer series
        break

    tmp = left
    cnt -= 1
    while left < M and valz[left] != 0:
        sumz -= lenz[left]
        left += 1
    if left < M:
        sumz -= lenz[left]
        cnt -= 1
        left += 1

out(maxsum)
