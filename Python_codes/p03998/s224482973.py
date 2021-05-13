import sys
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    S = {
        'a': list(input()),
        'b': list(input()),
        'c': list(input())
    }
    turn = 'a'
    while S[turn]:
        turn = S[turn].pop(0)
    print(turn.upper())

if __name__ == '__main__':
    main()
