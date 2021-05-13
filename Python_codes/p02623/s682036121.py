def solve():
    N,M,K = [int(i) for i in input().split()]

    A = [int(i) for i in input().split()]
    cumulative_A = [0] * (len(A)+1)
    for i in range(1, len(cumulative_A)):
        cumulative_A[i] = cumulative_A[i-1] + A[i-1]

    B = [int(i) for i in input().split()]
    cumulative_B = [0] * (len(B)+1)
    for i in range(1, len(cumulative_B)):
        cumulative_B[i] = cumulative_B[i-1] + B[i-1]

    max_j = len(cumulative_B) - 1
    ans = 0
    for i in range(len(cumulative_A)):
        time_A = cumulative_A[i]
        time_B = K - time_A
        is_found = False
        for j in reversed(range(max_j+1)):
            if cumulative_B[j] <= time_B:
                is_found = True
                break
        if is_found:
            cnt = i + j
            ans = max(cnt, ans)
        max_j = j

    print(ans)

if __name__ == "__main__":
    solve()