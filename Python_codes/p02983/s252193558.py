def main():
    L, R = map(int, input().split())
    if R//2019 - L//2019 > 1:
        print(0)
        return
    elif R//2019 == L//2019:
        U = list(range(L%2019, R%2019+1))
    else:
        print(0)
        return
    ans = 2019
    for i in U:
        for j in U:
            if i == j:
                continue
            ans = min(ans, (i*j)%2019)
    print(ans)


if __name__ == "__main__":
    main()
