N = int(input())
L = list(map(int, input().split()))
T = 0
if N > 2:
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                a = L[i]
                b = L[j]
                c = L[k]
                abc = sorted(list({a, b, c}))
                if len(abc) == 3 and abc[0] + abc[1] > abc[2]:
                    T += 1
print(T)