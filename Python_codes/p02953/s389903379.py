def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    highest = h_list[0]
    is_able = True

    for h in h_list:
        if highest > h:
            is_able = False
            break

        if highest + 1 < h:
            highest = h - 1

    if is_able:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
