import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    a = tuple(map(int, input().split()))

    ave = sum(a)/N
    ls = [abs(ave - i) for i in a]
    print(ls.index(min(ls)))

if __name__ == '__main__':
    main()
