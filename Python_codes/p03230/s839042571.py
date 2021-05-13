N = int(input())

k = 1

while 2*N >= k*(k-1):
    if 2*N == k*(k-1):
        print('Yes')
        print(k)

        S = [[0 for i in range(k-1)] for j in range(k)]

        for lis in range(k-1):
            S[0][lis] = lis + 1

        num_max = k - 1
        for history in range(1, k):
            num_max += k - 1 - history
            for bef_list in range(history):
                S[history][bef_list] = S[bef_list][history - 1]
            for new_list in range(k - history - 1):
                S[history][new_list + history] = num_max - new_list
            S[history].sort()

        for i in range(k):
            print(k-1, end=' ')
            for j in range(k-1):
                print(S[i][j], end=' ')
            print('')

        exit()

    k += 1

print('No')

