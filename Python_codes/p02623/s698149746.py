if __name__ == '__main__':
    N, M, K = map(int, input().split()) 
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    acc_A = []
    acc_B = []
    acc_A.append(0)
    acc_B.append(0)
    
    sum_a = 0
    sum_b = 0

    for a in A:
        sum_a += a
        acc_A.append(sum_a)

    for b in B:
        sum_b += b
        acc_B.append(sum_b)

    large_ar = []
    small_ar = []

    if N > M:
        large_ar = acc_A
        small_ar = acc_B
    else:
        large_ar = acc_B
        small_ar = acc_A
    
    ans = 0
    for i in range(len(small_ar)):
        for j in range(ans-i+1, len(large_ar)):
            if large_ar[j] + small_ar[i] <= K:
                ans = max(ans, i+j)
            else: break
    print(ans)