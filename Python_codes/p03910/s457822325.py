N = int(input())

W = 0

for i in range(1, N+1):
    W += i
    if W >= N:
        for j in range(1, i+1):
            if j != (W - N):
                print(j)
        break