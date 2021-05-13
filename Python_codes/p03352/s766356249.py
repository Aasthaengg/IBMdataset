import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    x = I()
    flag = [False]*(x+1)
    flag[1] = True
    for b in range(1, x+1):
        for p in range(2, x+1):
            temp = b**p
            if temp > x:
                break
            flag[temp] = True
    for i in range(x, 0, -1):
        if flag[i]:
            print(i)
            break

if __name__ == '__main__':
    main()