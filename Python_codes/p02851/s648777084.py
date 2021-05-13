def read():
    N, K = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    return N, K, A

def solve(N, K, A):
    if K == 1:
        return 0
    
    S = [0 for _ in range(N+1)]
    for i in range(N):
        S[i+1] = S[i] + A[i]
    
    count_sum = 0
    count = dict()
    for j in range(1, N+1):
        j_mod_k = (S[j] - j) % K  # 0 <= jmodk < K
        if j == 1:
            for i in range(max(0, j-K+1), j):
                # (S[i] - i) % K の値 i_mod_k は、次のループでもほぼ重複する
                # i = max(0, j-K+1) の時の i_mod_k は、i+1で破棄する
                # i = j の時の i_mod_k は、i+1で生成する
                i_mod_k = (S[i] - i) % K
                if i_mod_k in count:
                    count[i_mod_k] += 1
                else:
                    count[i_mod_k] = 1
        else:
            if max(0, j-K+1) != max(0, (j-1)-K+1):
                i = max(0, (j-1)-K+1)
                i_mod_k = (S[i] - i) % K
                if i_mod_k in count:
                    if count[i_mod_k] == 1:
                        count.pop(i_mod_k)
                    else:
                        count[i_mod_k] -= 1
            i = j-1
            i_mod_k = (S[i] - i) % K
            if i_mod_k in count:
                count[i_mod_k] += 1
            else:
                count[i_mod_k] = 1
        if j_mod_k in count:
            count_sum += count[j_mod_k]
    return count_sum

if __name__ == '__main__':
    inputs = read()
    print('%d' % solve(*inputs))
