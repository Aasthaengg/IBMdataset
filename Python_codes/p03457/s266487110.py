import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    pos = (0, 0)
    time_before = 0
    can = True

    for i in range(n):
        t, x, y = map(int, input().split())
        dist = abs(pos[0] - x) + abs(pos[1] - y)
        time = t - time_before
        # 時間内に到達不可
        if dist > time:
            can = False
            break
        if (dist % 2 == 0 and time % 2 != 0) or (dist % 2 != 0 and time % 2 == 0):
            can = False
            break
        time_before = t
        pos = (x, y)
    print('Yes' if can else 'No')

if __name__ == '__main__':
    main()
