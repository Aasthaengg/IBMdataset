N, L = map(int,input().split())

aji = 1000
sum = 0

for i in range(N):
    sum += L+i
    aji = min(aji, abs(L+i))
    if aji == abs(L+i):
        eat = i

print(sum - (L+eat))