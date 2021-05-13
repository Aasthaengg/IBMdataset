h, w, num = map(int, input().split())
a = [input() for _ in range(h)]
ans = 0

for j in range(2**h):
    b1 = ['-']*h
    for k in range(h):
        if ((j>>k)&1):
            b1[h-1-k] = '+'
    for i in range(2**w):
        b2 = ['-']*w
        for k in range(w):
            if ((i>>k)&1):
                b2[w-1-k] = '+'
        val = 0
        for n in range(h):
            for m in range(w):
                if b1[n] == '-' and b2[m] == '-' and a[n][m] == '#':
                    val += 1
        if val == num:
            ans += 1
print(ans)                        

        
