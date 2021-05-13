import sys
def input(): return sys.stdin.readline().strip()

def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    if n <= k:
        print(x * n)
    else:
        print(x * k + (n - k) * y)

if __name__ == "__main__":
    main()
