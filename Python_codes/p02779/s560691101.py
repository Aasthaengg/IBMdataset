def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    flag = True

    for i in range(n - 1):
        if a_list[i] == a_list[i + 1]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
