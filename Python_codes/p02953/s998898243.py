N = int(input())
H = list(map(int, input().split()))
I = [H[i + 1] - H[i] for i in range(N - 1)]
N = len(I)
for i in range(N):
    if I[i] >= 0:
        continue
    elif I[i] < -1:
        print('No')
        quit()
    else:
        if i == N - 1:
            continue
        for j in range(i + 1, N):
            if I[j] >= 1:
                break
            elif I[j] <= -1:
                print('No')
                quit()
            else:
                continue
print('Yes')