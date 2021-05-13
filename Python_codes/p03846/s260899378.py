from collections import Counter

N = int(input())
lst = [int(x) for x in input().split()]
counter = Counter(lst)

if N % 2 == 0:
    if len(counter) * 2 != N:
        print(0)
        exit()
    for x in range(1, N, 2):
        if counter[x] != 2:
            print(0)
            exit()

else:
    if len(counter) * 2 - 1 != N:
        print(0)
        exit()
    if counter[0] != 1:
        print(0)
        exit()
    for x in range(2, N + 1, 2):
        if counter[x] != 2:
            print(0)
            exit()

print(2 ** (N // 2) % (10 ** 9 + 7))