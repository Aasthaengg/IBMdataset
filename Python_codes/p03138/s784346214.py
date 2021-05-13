n,k = map(int,input().split())
A = list(map(int,input().split()))
cnt = [0]*50
for a in A:
    i = 0
    while a > 0:
        if a&1:
            cnt[i] += 1
        i += 1
        a = a >> 1
base = 0
delta = [0]*50
pow2 = 1
s = [0]*51
for i,c in enumerate(cnt):
    delta[i] = max(0,pow2*(n - 2*c))
    base += pow2*c
    s[i+1] = s[i] + delta[i]
    pow2*=2
i = 0
K = []
ans = 0
while k > 0:
    if k&1:
        K.append(i)
        ans += delta[i]
    i += 1
    k = k >> 1
done = 0
for i in K[::-1]:
    ans = max(ans, done + s[i])
    done += delta[i]
print(ans + base)
