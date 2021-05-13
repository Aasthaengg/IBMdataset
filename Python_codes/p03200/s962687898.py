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
    S = input()
    l = []
    for i in range(len(S)):
        if S[i] == 'W':
            l.append(i-len(l))
    print(sum(l))


if __name__ == '__main__':
    main()
