N, K = map(int, input().split())
S = input()
S = '1' + S + '1'
rev = []
for i in range(N+1):
    if S[i] != S[i+1]:
        rev.append(i)
l = len(rev)//2
a = [(rev[2*i], rev[2*i+1]) for i in range(l)]

a = [(0, 0)] + a + [(N, N)]
K = min(K, l)

m = -1
for i in range(l-K+1):
    x = a[i+K+1][0]-a[i][1]
    m = max(m, x)

print(m)