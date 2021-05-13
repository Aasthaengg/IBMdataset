import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    c = [list(mi()) for i in range(3)]
    if c[0][0]+c[1][1] == c[0][1]+c[1][0] \
        and c[1][1]+c[2][2] == c[1][2]+c[2][1] \
        and c[2][2]+c[0][0] == c[2][0]+c[0][2]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
