N = int(input())
A = list(map(int, input().split()))
A2 = []
Z = []
ans = 0
zerocnt = 0
for ai in A:
    if ai == 0:
        zerocnt += 1
    elif zerocnt >= 1:
        A2 += [0]
        Z += [zerocnt]
        ans += (zerocnt * (zerocnt+1)) // 2
        zerocnt = 0
    if ai != 0:
        A2 += [ai]
        Z += [1]
        ans += 1

if zerocnt >= 1:
    A2 += [0]
    Z += [zerocnt]
    ans += (zerocnt * (zerocnt+1)) // 2
    zerocnt = 0

for i, ai in enumerate(A2):
    aixor = ai
    sumA = ai
    for j in range(i+1, min(i+41, len(A2))):
        aj = A2[j]
        aixor = aixor ^ aj
        sumA += aj
        if aixor != sumA:
            break
        else:
            ans += (Z[i] * Z[j])
        
print(ans)