N = int(input())

N_h_place = N // 100
N_o_place = N % 10

ans = 'No'

if N_h_place == N_o_place:
    ans = 'Yes'

print(ans)
