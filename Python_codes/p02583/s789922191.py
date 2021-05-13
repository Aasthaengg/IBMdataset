N = int(input())
hen = list(map(int, input().split()))

kosu = 0

if N <= 2:
    print(kosu)

else:
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if hen[i] != hen[j] and hen[j] != hen[k] and hen[k] != hen[i]\
                and hen[i] + hen[j] > hen[k] and hen[k] + hen[i] > hen[j] and hen[j] + hen[k] > hen[i]\
                and i < j < k:
                    kosu += 1

    print(kosu)