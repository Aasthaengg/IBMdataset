def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    num_list = [0] * n  # 各番号が書かれたボールが何個あるか
    method_list = [0] * n  # 同じ番号が書かれた異なる2つのボールを選ぶ方法

    for a in a_list:
        num_list[a - 1] += 1

    for i in range(n):
        b = num_list[i]
        if b >= 2:
            method_list[i] = b * (b - 1) // 2

    total_method = sum(method_list)

    for k in range(n):
        c = a_list[k]  # k番目のボールに書かれている数字
        ans = total_method - method_list[c - 1]
        d = num_list[c - 1]
        if d >= 3:
            e = (d - 1) * (d - 2) // 2
        else:
            e = 0
        ans += e
        print(ans)


if __name__ == "__main__":
    main()
