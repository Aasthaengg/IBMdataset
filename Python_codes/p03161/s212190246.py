if __name__ == '__main__':
    N, K = map(int, input().split())
    h_list = list(map(int, input().split()))
 
    dp_list = [0]
    for n in range(1, N):
        tmp_h = h_list[n]
        if n < K:
            lst = [abs(tmp_h - h_list[i]) + dp_list[i] for i in range(n)]
        else:
            lst = [abs(tmp_h - h_list[n-k]) + dp_list[n-k] for k in range(1, K + 1)]
        dp_list.append(min(lst))
    print(dp_list[-1])