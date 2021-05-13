MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n = int(input())
    s = []
    if n == 0:
        print('0')
        return

    while n != 0:
        if n%2 == 0:
            s.append('0')
            n //= -2
        else:
            s.append('1')
            n -= 1
            n //= -2
    print(''.join(s[::-1]))

if __name__ =='__main__':
    main()   