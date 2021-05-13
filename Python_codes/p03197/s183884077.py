import sys
def input(): return sys.stdin.readline().strip()
def main():
    N = int(input())
    A = (int(input()) for _ in range(N))
    print("second") if all(( a%2==0 for a in A)) else print("first")
if __name__ == "__main__":
    main()