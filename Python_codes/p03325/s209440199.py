import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for a in A:
        while a % 2 == 0:
            cnt += 1
            a //= 2
    print(cnt)

if __name__ == "__main__":
    main()
