def main():
    o, e = input(), input()
    len_o, len_e = len(o), len(e)
    ans = ""

    for i in range(len_e * 2):
        if i % 2 == 0:
            ans += o[i // 2]
        else:
            ans += e[i // 2]

    if len_o == len_e + 1:
        ans += o[-1]

    print(ans)


if __name__ == "__main__":
    main()
