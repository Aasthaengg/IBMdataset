a, b, k = map(int, input().split())
takahashi = a
aoki = b
for i in range(k):
    if i%2 == 0:
        takahashi = takahashi//2
        aoki += takahashi
    else:
        aoki = aoki//2
        takahashi += aoki
print(takahashi, aoki)