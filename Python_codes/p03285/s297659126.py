import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    for b in range(N // 7, -1, -1):
        a = N - 7 * b
        if a % 4 == 0:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
