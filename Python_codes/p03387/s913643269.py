L = list(map(int, input().split()))
L.sort()

ans = L[2]-L[1]
L[0] = L[0]+ L[2]-L[1]
L[1] = L[2]
if L[0]%2 == L[2]%2:
    ans += (L[2]-L[0])//2
else:
    ans += 1 + (L[2]+1-L[0])//2
print(ans)
