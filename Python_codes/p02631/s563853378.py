def main():
        

    N = int(input())
    A_s = list(map(int, input().split()))

    all_xor = A_s[0]

    for i in range(1, N):
        all_xor = (all_xor ^ A_s[i])

    ans_list = []

    for i in range(N):
        ans = (all_xor ^ A_s[i])
        ans_list.append(ans)

    print(' '.join(map(str, ans_list)))


if __name__ == '__main__':
    main()
