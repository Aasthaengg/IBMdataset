import sys
def input(): return sys.stdin.readline().strip()


def main():
    g1 = [1,3,5,7,8,10,12]
    g2 = [4,6,9,11]
    g3 = [2]
    d = {}
    for x in g1: d[x] = 1
    for x in g2: d[x] = 2
    for x in g3: d[x] = 3
    x, y = map(int, input().split())
    if d[x] == d[y]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
