def main():
    abc = sorted(list(map(int, input().split())))

    cnt = 0
    while True:
        if abs(abc[2] - abc[0]) <= 1 and abs(abc[2] - abc[0]) <= 1:
            break
        abc[0] += 2
        abc = sorted(abc)
        cnt += 1
    ans = cnt
    if abc[0] == abc[1] and abc[1] == abc[2]:
        ans = cnt
    elif abc[2] == abc[1]:
        ans += 2
    elif abc[0] == abc[1]:
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
