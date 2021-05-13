import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    pre_t = 0
    pre_x = 0
    pre_y = 0
    for _ in range(n):
        t, x, y = map(int, input().split())
        d_dis = abs(x - pre_x) + abs(y - pre_y)
        d_t = abs(t - pre_t)
        if d_dis > d_t:
            print('No')
            sys.exit()
        elif (d_t - d_dis) % 2 == 1:
            print('No')
            sys.exit()
        else:
            pre_t = t
            pre_x = x
            pre_y = y
    print('Yes')

if __name__ == '__main__':
    main()
