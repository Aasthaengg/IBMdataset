import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    h = LI()
    for i in range(n-1, 0, -1):
        diff = h[i] - h[i-1]
        if diff >= 0:
            continue
        elif diff == -1:
            h[i-1] -= 1
        else:
            print("No")
            sys.exit()
    print("Yes")

if __name__ == '__main__':
    main()