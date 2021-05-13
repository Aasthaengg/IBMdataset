def solve():
    N, M = list(map(int, input().split()))
    H = list(map(int, input().split()))
    R = []
    for _ in range(M):
        R.append(list(map(int, input().split())))
    Check_array = [1 for _ in range(N)]
    for r in R:
        if(H[r[0]-1] < H[r[1]-1]):
            Check_array[r[0] - 1] = 0
        elif (H[r[0]-1] > H[r[1]-1]):
            Check_array[r[1] - 1] = 0
        else:
            Check_array[r[0] - 1] = 0
            Check_array[r[1] - 1] = 0
    print(sum(Check_array))


if __name__ == "__main__":
    solve()
