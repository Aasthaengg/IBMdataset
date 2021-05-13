import sys
def input(): return sys.stdin.readline().strip()


def main():
    x = int(input())
    if x < 1200:
        print("ABC")
    else:
        print("ARC")

if __name__ == "__main__":
    main()
