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
    O = input()
    E = input()
    ans = ''
    for i in range(len(O)+len(E)):
        if i%2:
            ans += E[i//2]
        else:
            ans += O[i//2]

    print(ans)



if __name__ == '__main__':
    main()
