import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    d = []
    e = []
    for k in range(N):
        x, y = map(int,input().split())
        d.append(x+y)
        e.append(x-y)
    d.sort()
    e.sort()
    print(max(e[-1]-e[0],d[-1]-d[0]))

if __name__ == '__main__':
    main()
