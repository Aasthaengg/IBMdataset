# nikkei2019-qualB - Touitsu
def main():
    n = int(input())
    S = [input().rstrip() for _ in range(3)]
    ans = 0
    for i in zip(S[0], S[1], S[2]):
        if len(set(i)) == 3:
            ans += 2
        elif len(set(i)) == 2:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()