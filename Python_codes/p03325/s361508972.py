import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    A = LI()
    cnt = 0
    for a in A:
        while a%2 == 0:
            cnt += 1
            a //= 2
    print(cnt)

if __name__ == '__main__':
    main()