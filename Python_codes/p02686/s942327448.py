#!python3

def LI():
    return list(map(int, input().split()))

# input
N = int(input())
S = [input() for _ in range(N)]


def judge(v):
    x = 0
    for b, l in v:
        if x + b < 0:
            return False
        x += l
    return True


def main():
    pl, ml = [], []
    t = 0
    for i in range(N):
        l = 0
        b = 0
        for s in S[i]:
            if s == "(":
                l += 1
            else:
                l -= 1
                b = min(b, l)
        t += l
        if l > 0:
            pl.append((b, l))
        else:
            ml.append((b - l, -l))

    pl.sort(reverse=True)
    ml.sort(reverse=True)

    if judge(pl) and judge(ml) and t == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
