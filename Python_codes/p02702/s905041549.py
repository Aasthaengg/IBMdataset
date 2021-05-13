S = list(map(int, list(input())))
S.reverse()
a = [0]*len(S)
y = 2019
x = 1
t = 0
cnt = [0]*y
res = 0
for i in range(len(S)):
    cnt[t] += 1
    t += S[i]*x
    t %= y
    res += cnt[t]
    x = x*10%y
print(res)