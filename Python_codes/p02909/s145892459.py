def main():
    S = input()

    lst = ["Sunny", "Cloudy", "Rainy", "Sunny"]

    for i in range(len(lst)):
        if S == lst[i]:
            ans = lst[i + 1]
            break

    print(ans)


if __name__ == "__main__":
    main()
