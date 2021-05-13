import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))

def main():
    h, w = MI()
    s = []
    for _ in range(h):
        s.append(list(input()))
    for i in range(h):
        for j in range(w):
            flag = False
            if s[i][j] == '.':
                continue
            if i == 0 and j == 0:
                flag |= s[i][j+1] == '#'
                flag |= s[i+1][j] == '#'
            elif i == 0 and j == w-1:
                flag |= s[i+1][j] == '#'
                flag |= s[i][j-1] == '#'
            elif i == h-1 and j == 0:
                flag |= s[i-1][j] == '#'
                flag |= s[i][j+1] == '#'
            elif i == h-1 and j == w-1:
                flag |= s[i-1][j] == '#'
                flag |= s[i][j-1] == '#'
            elif i == 0:
                flag |= s[i][j+1] == '#'
                flag |= s[i+1][j] == '#'
                flag |= s[i][j-1] == '#'
            elif i == h-1:
                flag |= s[i-1][j] == '#'
                flag |= s[i][j+1] == '#'
                flag |= s[i][j-1] == '#'
            elif j == 0:
                flag |= s[i-1][j] == '#'
                flag |= s[i][j+1] == '#'
                flag |= s[i+1][j] == '#'
            elif j == w-1:
                flag |= s[i-1][j] == '#'
                flag |= s[i+1][j] == '#'
                flag |= s[i][j-1] == '#'
            else:
                flag |= s[i-1][j] == '#'
                flag |= s[i][j+1] == '#'
                flag |= s[i+1][j] == '#'
                flag |= s[i][j-1] == '#'
            if not flag:
                print("No")
                sys.exit()
    print("Yes")

if __name__ == '__main__':
    main()