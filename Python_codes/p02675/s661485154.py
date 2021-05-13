def main():
    N = input()

    if N[-1] == "3":
        ans = "bon"
    elif N[-1] == "0" or N[-1] == "1" or N[-1] == "6" or N[-1] == "8":
        ans = "pon"
    else:
        ans = "hon"

    print(ans)


if __name__ == "__main__":
    main()
