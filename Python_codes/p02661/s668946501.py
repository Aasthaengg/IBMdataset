
N = int(input())
L, H = [0] * N, [0] * N

for i in range(N):
    L[i], H[i] = list(map(int, input().split()))

L.sort()
H.sort(reverse=True)
if N%2 == 1:
    i = (N-1)//2
    l, h = L[i], H[i]
    print(h-l+1)
else:
    i = N//2
    ll, lh = L[i-1], L[i]
    hl, hh = H[i-1], H[i]
    print((hh+hl) - (lh+ll) + 1)

