N = input()
N_list = list(N)
N = int(N)
K = len(N_list)

ans = int(N_list[0])+(K-1)*9
ans_list = [N_list[0]] + ['9' for _ in range(K-1)]
ans_cand = int(''.join(ans_list))
if N < ans_cand:
    print(ans - 1)
else:
    print(ans)