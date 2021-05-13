def nC2(n):
    return n * (n - 1) // 2


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    cnt_list = [0] * n  # 各番号が書かれたボールが何個あるか

    for a in a_list:
        cnt_list[a - 1] += 1

    total_method = 0
    for i in range(n):
        total_method += nC2(cnt_list[i])

    for k in range(n):
        ans = total_method
        num_k = cnt_list[a_list[k] - 1]  # k番目のボールに書かれた数字が何個あるか
        ans -= nC2(num_k)
        num_k -= 1
        ans += nC2(num_k)
        print(ans)


if __name__ == "__main__":
    main()
