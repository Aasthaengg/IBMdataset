n = int(input())
h = list(map(int, input().split()))
def water(l, r, sub):
    if l == r:
        return 0
    i = l + h[l:r].index(min(h[l:r]))
    a = water(l, i, h[i]) 
    b = water(i + 1, r, h[i])
    return h[i] - sub + a + b
print(water(0, n, 0))