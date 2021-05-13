# nikkei2019-qualB - Touitsu
def main():
    N, *S = open(0).read().split()
    ans = 0
    for i in zip(*S):
        x = len(set(i))
        if x == 3:
            ans += 2
        elif x == 2:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()