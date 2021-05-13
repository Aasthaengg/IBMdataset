h,w,k = map(int,input().split())
lay = ['']*h
ans = 0
for i in range(h):
    lay[i] = input()
for i in range(2**h):
    for j in range(2**w):
        #行と列を選択した
        kuro = 0
        for i2 in range(h):
            if (i>>i2) & 1:
                for j2 in range(w):
                    if (j>>j2) & 1:
                        if lay[i2][j2] == '#':
                            kuro += 1
        if kuro == k:
            ans += 1
print(ans)