N,K = map(int,input().split())
p = list(map(int,input().split()))

rwa = [0]*(len(p)+1)

for i in range(len(rwa)-1):
    rwa[i+1] = rwa[i]+p[i]

wa = [0]*(N-K+1)
for i in range(len(wa)):
    wa[i] = rwa[K+i]-rwa[i]

t = wa.index(max(wa))

re = 0
for i in range(K):
    if p[t+i]%2 == 0:
        re += p[t+i]/2 +0.5
    else:
        re += p[t+i]//2 +1


print(re)
