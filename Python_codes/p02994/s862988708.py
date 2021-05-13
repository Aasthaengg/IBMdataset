N, L = map(int, input().split())

apples = []
for i in range(1, N+1):
    apples.append(L+i-1)

tast = sum(apples)
for i in range(500):
    if i in apples:
        tast -= i
        break
    elif -i in apples:
        tast += i
        break
print(tast)

