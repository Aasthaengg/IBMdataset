N = int(input())
N_str = str(N)

for i in range(len(N_str) // 2):
    if N_str[i] != N_str[len(N_str) -1 - i]:
        print('No')
        exit()
print('Yes')