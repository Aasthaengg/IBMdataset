import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    T = LI()
    A = LI()
    B = LI()

    p1 = (A[0] - B[0]) * T[0]
    p2 = p1 + (A[1] - B[1]) * T[1]
    if p1 * p2 > 0:
        print(0)
        return
    elif p2 == 0:
        print('infinity')
        return

    ans = 1
    p2 = abs(p2)
    p1 = abs(p1)
    if p1 % p2 == 0:
        ans -= 1
    ans += (p1 // p2) * 2
    print(ans)

if __name__ == '__main__':
    main()