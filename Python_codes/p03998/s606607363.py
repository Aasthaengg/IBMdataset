import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    sa = input()
    sb = input()
    sc = input()
    la, lb, lc = len(sa), len(sb), len(sc)
    ia, ib, ic = 0, 0, 0
    turn = 'a'
    while True:
        if turn == 'a':
            if ia == la:
                print('A')
                break
            turn = sa[ia]
            ia += 1
        elif turn == 'b':
            if ib == lb:
                print('B')
                break
            turn = sb[ib]
            ib += 1
        else:
            if ic == lc:
                print('C')
                break
            turn = sc[ic]
            ic += 1

if __name__ == '__main__':
    main()