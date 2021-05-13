N = list(input())
N_int = [int(n) for n in N]
cnt = 0

for i in range(len(N_int)-1):
    if N_int[i+1] != 9:
        N_int[i] -= 1
        for j in range(i+1, len(N_int)):
            N_int[j] = 9

for i in N_int:
    cnt += int(i)

print(cnt)