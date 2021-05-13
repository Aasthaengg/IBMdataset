N, M = map(int,input().split())
KA = []
for n in range(N):
    KA.append([ka for ka in map(int,input().split())])

ans = set(range(1,M+1))

for ka in KA:
    ans = ans & set(ka[1:])

print(len(ans))