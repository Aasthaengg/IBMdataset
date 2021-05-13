N = int(input())

for N_l in range(1,10):
    for N_r in range(1,10):
        if N_l * N_r == N:
            print('Yes')
            exit()
print('No')