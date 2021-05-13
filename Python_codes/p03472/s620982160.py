N, H = map(int, input().split())
# B = []
A = []
B = []
amax = -1
bmax = -1

for _ in range(N):
    a, b = map(int, input().split())
    # B.append((a,b))
    A.append(a)
    B.append(b)

    if amax < a:
        amax = a
    
    if bmax < b:
        bmax = b

if amax >= bmax:
    m = H % amax
    if m != 0:
        ans = H // amax + 1
    else:
        ans = H // amax

else:
    ans = 0
    throw_lst = list(filter(lambda x: x > amax, B))
    throw_lst.sort(reverse=True)

    for tb in throw_lst:
        H -= tb
        ans += 1
        if H <= 0:
            print(ans)
            exit(0)

    m = H % amax
    if m != 0:
        ans += H // amax + 1
    else:
        ans += H // amax

print(ans)