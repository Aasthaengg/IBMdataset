p = list(map(int, input().split()))

k = 0
for i in range(p[0]):
    ab = list(map(int, input().split()))
    if ab[0] >= p [1] and ab[1] >= p[2]:
        k += 1

print(k)