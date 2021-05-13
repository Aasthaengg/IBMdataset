N, M = map(int, input().split())
S_array = list(map(int, input().split()))
T_array = list(map(int, input().split()))

mod = 10**9 + 7

add_num_array = [0] * N
ans_array = [0] * (N + 1)
ans_old = [1] * (N + 1)

for t in T_array:
    ans_array = [1] * (N+1)
    for i, s in enumerate(S_array):
        if s == t:
            add_num_array[i] = (add_num_array[i] + ans_old[i]) % mod
        ans_array[i + 1] = (ans_array[i] + add_num_array[i]) % mod
    ans_old = ans_array

print(ans_array[-1])