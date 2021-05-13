import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def switch(n):
    if n == '1':
        return '9'
    elif n == '9':
        return '1'
    else:
        return n


def main():
    N = ns()
    ans = ''
    for n in N:
        ans += switch(n)
    print(ans)


if __name__ == '__main__':
    main()
