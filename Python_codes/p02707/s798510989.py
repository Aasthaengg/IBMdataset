if __name__ == "__main__":
    N = int(input())
    buka_num_arr = [0] * N
    joshi_idx_arr = list(map(int,input().split()))
    for joshi_idx in joshi_idx_arr:
        buka_num_arr[joshi_idx-1] += 1
    for i in range(N):
        print(buka_num_arr[i])