

def main():
    s = input()
    cnt = 0
    for i in range(3):
        if s[i] == 'o':
            cnt += 1
    print(700 + 100 * cnt)


if __name__ == "__main__":
    main()
