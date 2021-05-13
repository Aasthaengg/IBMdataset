N = int(input())
results = ''
for A in range(N + 1):
    if A == 0:
        continue

    BBB = []
    AAA = []

    B = N - A
    if B >= 1:
        for b in range(len(str(B))):
            BBB.append(int(str(B)[b]))

        for a in range(len(str(A))):
            AAA.append(int(str(A)[a]))
        sums = sum(BBB) + sum(AAA)
        if sums == 1:
            print(A)
            print(B)
            print(AAA)
            print(BBB)

        if not results:
            results = sums
        else:
            if results > sums:
                results = sums
print(results)