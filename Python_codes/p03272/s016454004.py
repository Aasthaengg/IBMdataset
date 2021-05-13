N, i = map(int, input().split())
N_list = list(range(1, N+1))
N_list.reverse()
for j in range(N):
    if i == N_list[j]:
        print(j+1)
