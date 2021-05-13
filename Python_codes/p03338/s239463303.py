N = int(input())
S = list(input())
ans = 0
for i in range(N):
    a = S[:i]
    b = S[i:]
    aset = set(a)
    bset = set(b)
    count = 0
    for i in aset:
        if i in bset:
            count += 1
    ans = max(ans,count)
print(ans)