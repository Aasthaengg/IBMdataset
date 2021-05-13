n = int(input())
h = [int(i) for i in input().split()]
sikiri = [-1, n]
ans = 0

for i in range(max(h)+1): # i は高さ
    sik = [j for j, x in enumerate(h) if x == i]
    sikiri[len(sikiri):len(sikiri)] = sik
    sikiri.sort()
    
    for j in range(len(sikiri)-1):
        if sikiri[j+1] - sikiri[j] > 1:
            ans += 1
        else:
            pass
print(ans)