N = int(input())
for k in range(N+2):
    if k * (k-1) == 2 * N:
        S = [[] for _ in range(k+1)]
        n = 1
        for i in range(2, k+1):
            for j in range(1, i):
                S[i].append(n)
                S[j].append(n)
                n += 1
        print('Yes')
        print(k)
        for i in range(1, k+1):
            ans = [len(S[i])] + S[i]
            print(' '.join(map(str, ans)))
        exit()
print('No')