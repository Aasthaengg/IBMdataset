def main():
    s = input()
    ans = 0
    correct = "CODEFESTIVAL2016"
    for i in range(16):
        if s[i] != correct[i]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()

