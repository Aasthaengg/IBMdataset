# AGC020B - Ice Rink Game
def main():
    K, *A = map(int, open(0).read().split())
    l, h = 2, 2  # low, high
    for i in A[::-1]:
        l += -l % i
        h += i - 1 - h % i
    if l > h:
        print(-1)
    else:
        print(l, h)


if __name__ == "__main__":
    main()