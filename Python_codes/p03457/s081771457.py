import sys
from math import sqrt
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    possible = True
    pre_t, pre_x, pre_y = 0, 0, 0
    for _ in range(n):
        t, x, y = map(int, input().split())
        dist = abs(x - pre_x) + abs(y - pre_y)
        time = t - pre_t
        #print("dist={}".format(dist))
        if dist <= time and (time - dist) % 2 == 0:
            pre_t, pre_x, pre_y = t, x, y
        else:
            possible = False
            break
    if possible:
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
    main()
