import sys
def input(): return sys.stdin.readline().strip()


def main():
    x, a, b = map(int, input().split())
    if a >= b:
        print("delicious")
    elif (b - a) <= x:
        print("safe")
    else:
        print("dangerous")



if __name__ == "__main__":
    main()
