# AGC020B - Ice Rink Game
def main():
    K, *A = map(int, open(0).read().split())
    if A.pop() != 2:
        print(-1)
        return
    mn, mx = 2, 3
    for i in A[::-1]:
        if i > mx:
            print(-1)
            return
        mx = mx // i * i + i - 1
        mn = ((mn + i - 1) // i) * i
    if mn > mx:
        print(-1)
    else:
        print(mn, mx)


if __name__ == "__main__":
    main()