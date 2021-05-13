x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
goukei = []
for a in A:
    for b in B:
        goukei.append(a + b)
goukei.sort()
goukei2 = goukei[-k:]
goukei3 = []
for c in C:
    for ab in goukei2:
        goukei3.append(ab + c)
goukei3.sort(reverse=True)
print(*goukei3[:k], sep="\n")
