import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    a = int(input())
    val = n % 500
    if val <= a: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()
