# yahoo-procon2019-qualB - Path
def main():
    *A, = map(int, open(0).read().split())
    cnt = [0] * 5
    for i in A:
        cnt[i] += 1
    flg = all(i < 3 for i in cnt[1:])
    print("YES" if flg else "NO")


if __name__ == "__main__":
    main()