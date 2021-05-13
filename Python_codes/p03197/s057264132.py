import sys
def input(): return sys.stdin.readline().strip()
def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print("first") if any([a%2 for a in A]) else print("second")
if __name__ == "__main__":
    main()