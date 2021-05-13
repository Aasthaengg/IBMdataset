import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    h, w = MI()
    s = [input() for _ in range(h)]
    table = [[0]*(w+2) for _ in range(h+2)]
    for i in range(1, h+1):
        for j in range(1, w+1):
            table[i][j] = s[i-1][j-1]
    for i in range(1, h+1):
        for j in range(1, w+1):
            if table[i][j] == '#':
                print('#', end='')
                continue
            cnt = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if table[k][l] == '#':
                        cnt += 1
            print(cnt, end='')
        print()

if __name__ == '__main__':
    main()