def main():
    N = int(input())
    S = input()
    ans = 0

    for i in range(10):
        for j in range(10):
            for k in range(10):
                i_index = S.find(str(i))
                if i_index == -1:
                    continue

                j_index = S.find(str(j), i_index + 1)
                if j_index == -1:
                    continue

                k_index = S.find(str(k), j_index + 1)
                if k_index != -1:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
