import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    h = sorted([int(input()) for i in range(N)], reverse=True)

    MAX = (h[0] // B) + 1

    l, r = 0, MAX
    while True:
        # print(l, r)
        if l + 1 >= r:
            print(r)
            break
        t = (l + r) // 2
        Bt = B * t
        a = 0
        i = 0
        while i < N and h[i] > Bt:
            tmp = h[i] - Bt
            if tmp % (A-B) == 0:
                a += tmp // (A-B)
            else:
                a += tmp // (A-B) + 1
            i += 1
        # print(t, a)
        if a <= t:# t回で倒しきれる
            l, r = l, t
        else:
            l, r = t, r

if __name__ == "__main__":
    main()