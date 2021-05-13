N, *A = map(int, open(0).read().split())
sorted_A = sorted(A)
for a in A:
    if a == sorted_A[-1]:
        print(sorted_A[-2])
    else:
        print(sorted_A[-1])
