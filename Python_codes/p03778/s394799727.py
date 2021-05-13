import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    w, a, b = MI()
    if b < a:
        temp = a
        a = b
        b = temp
    ans = max(0, b-a-w)
    print(ans)


if __name__ == '__main__':
    main()