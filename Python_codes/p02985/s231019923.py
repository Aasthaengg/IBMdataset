MOD = 10 ** 9 + 7

N,K = map(int,input().split())

perm = [0] * (10**5)
perm[0] = 1
for l in range(1,10 ** 5):
    perm[l] = (perm[l-1] * (K-l-1)) % MOD

info = [[] for _ in range(N)]

def intminus(t):
    return int(t)-1

for i in range(N-1):
    a,b = map(intminus,input().split())
    info[a].append(b)
    info[b].append(a)

count = 1

for j in range(1+len(info[0])):
    count = (count * (K-j)) % MOD

stack = []
for p in info[0]:
    stack.append([0,p])

while stack:
    x = stack.pop(-1)
    count = (count * perm[len(info[x[1]])-1]) % MOD
    for xx in info[x[1]]:
        if xx == x[0]:continue
        stack.append([x[1],xx])

print(count)