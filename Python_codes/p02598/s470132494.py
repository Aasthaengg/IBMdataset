def min_cut_num(n, L, size):
    cnt = 0
    for wood in L:
        cnt += ((wood + size - 1) // size) - 1
    return cnt
    

def main():
    n, k = map(int, input().split())
    L = list(map(int, input().split()))
    # k 回以内のカットで作成できる最小の上限サイズを特定する
    left = 0
    right = 10 ** 9    # 必ず k 回以内
    while right - left > 1:
        mid = (left + right) // 2
        if min_cut_num(n, L, mid) <= k:
            right = mid
        else:
            left = mid
    print(right)




if __name__ == '__main__':
    main()