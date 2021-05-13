n,m, x = map(int, input().split())

lis = list(map(int, input().split()))

nlis = [0]*(n+1)

for i in lis:
    nlis[i] = 1

ans = min(sum(nlis[:x]), sum(nlis[x:]))

print(ans)