import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    a = LI()
    color = 8
    free = 0
    flag = [False]*color
    for ai in a:
        if ai >= 3200:
            free += 1
        else:
            flag[ai//400] = True
    color_min = max(1, sum(flag))
    color_max = sum(flag)+free
    print("{} {}".format(color_min, color_max))

if __name__ == '__main__':
    main()