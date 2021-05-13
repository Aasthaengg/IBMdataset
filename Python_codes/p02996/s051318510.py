N = int(input())

L = []
B = []
A = []
for _ in range(N):
    a, b = map(int, input().split())
    L.append((a, b))
    B.append(b)
    A.append(a)

L.sort(key=lambda x: x[1])

max_B = max(B)
sum_A = sum(A)

if (sum_A > max_B):
    print('No')
    exit()
else:
    count = 0
    for i in range(N):
        count += L[i][0]

        if (count > L[i][1]):
            print('No')
            exit()
        else:
            continue

    print('Yes')
