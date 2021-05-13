def main():
    S = input().rstrip()
    for idx, s in enumerate(S, start=1):
        if idx % 2 == 1 and s not in ["R", "U", "D"]:
            print("No")
            exit()
        elif idx % 2 == 0 and s not in ["L", "U", "D"]:
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    main()
