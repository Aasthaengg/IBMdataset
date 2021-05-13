import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    A = LI()
    while True:
        ans = min(A)
        A = [x%ans for x in A if x%ans != 0]
        if not A:
            print(ans)
            break
        A.append(ans)


if __name__ == '__main__':
    main()