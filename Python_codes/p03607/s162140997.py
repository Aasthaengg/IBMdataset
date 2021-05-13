import sys
sys.setrecursionlimit(500000)

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
    N = ii()
    A = [ii() for _ in range(N)]
    dic = {}
    for a in A:
        if (not a in dic) or (dic[a] == 0):
            dic[a] = 1
        else:
            dic[a] = 0
    print(sum(dic.values()))


if __name__ == '__main__':
    main()
