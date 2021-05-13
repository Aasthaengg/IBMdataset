a,b,k = map(int, input().split())

ab = [a,b]
for i in range(k):
    p = i%2
    if ab[p]%2 == 1:
        ab[p] -= 1
    half = ab[p]/2
    ab[p] -= half
    ab[1-p] += half

print(int(ab[0]), int(ab[1]))
