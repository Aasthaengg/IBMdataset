s = input()
s = list(reversed(s))
n = len(s)
dp1 = [0]*n
dp2 = [0]*n
counting = [0]*2019
counting[0] += 1
dp1[0] = 1
dp2[0] = int(s[0])
counting[dp2[0]] += 1
if n >= 2:
    for i in range(1,n):
        dp1[i] = (10*dp1[i-1]) % 2019
        dp2[i] = (int(s[i])*dp1[i]+dp2[i-1]) % 2019
        counting[dp2[i]] += 1
sm = 0
for j in range(2019):
    sm += int(counting[j]*(counting[j]-1)/2)
print(sm)