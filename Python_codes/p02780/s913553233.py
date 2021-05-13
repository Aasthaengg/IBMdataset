def solve():
    N,K = [int(i) for i in input().split()]
    P = [int(i) for i in input().split()]
    prev_K_sum = max_K_sum = sum(P[:K])
    start = 0
    for i in range(N-K):
        cur_K_sum = prev_K_sum - P[i] + P[i+K]
        if cur_K_sum > max_K_sum:
            start = i + 1
            max_K_sum = cur_K_sum
        prev_K_sum = cur_K_sum
    target = P[start:start+K]
    ans = sum([(num+1)/2.0 for num in target])
    print(ans)

if __name__ == "__main__":
    solve()