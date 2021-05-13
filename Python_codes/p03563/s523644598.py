import sys
def input(): return sys.stdin.readline().strip()

def main():
    r = int(input())
    g = int(input())
    print(2 * g - r)


if __name__ == "__main__":
    main()
