n,m = map(int,input().split())

currency = sorted(map(int,input().split()))

gra = [float('inf')]*(n+1)
gra[0] = 0
for i in range(m):
    for j in range(currency[i],n+1):
        gra[j] = min(gra[j],gra[j-currency[i]]+1)

print(gra[n])