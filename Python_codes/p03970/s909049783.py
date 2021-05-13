def main():
    S = input()
    target = "CODEFESTIVAL2016"
    ans = 0
    for i, s in enumerate(S):
        if s != target[i]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
