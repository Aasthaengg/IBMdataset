def main():
    n = int(input())
    As = list(map(int, input().split()))
    fours = 0
    evens = 0
    odds = 0
    for A in As:
        if A % 4 == 0:
            fours += 1
        elif A % 2 == 0:
            evens += 1
        else:
            odds += 1

    if fours+(evens)//2 >= n//2:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
