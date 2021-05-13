import sys
input = sys.stdin.readline
def main():
    Wr, Hu, N = map(int, input().split())
    C =  [list(map(int, input().split())) for i in range(N)]
    Wl, Hd = 0, 0
    for x, y ,a in C:
        if a == 1:
            if Wl <= x:
                Wl = x
        if a == 2:
            if Wr >= x:
                Wr = x
        if a == 3:
            if Hd <= y:
                Hd = y
        if a == 4:
            if Hu >= y:
                Hu = y
        if Wr <= Wl or Hu <= Hd:
            print(0)
            return
    W = Wr - Wl
    H = Hu - Hd
    print(W*H)

if __name__ == '__main__':
    main()