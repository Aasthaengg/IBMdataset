import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = input()
    if N[0] == N[-1]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
