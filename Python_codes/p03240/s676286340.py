import sys
MOD = 10**9 + 7
# import io, os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input():
    return sys.stdin.readline()[:-1]

def main():
    n = int(input())
    p = [list(map(int,input().split())) for _ in range(n)]
    p = sorted(p,key=lambda x: -x[2])
    for x in range(0,101):
        for y in range(0,101):
            h = p[0][2] + abs(x-p[0][0]) + abs(y-p[0][1])
            flag = 1
            for (a,b,c) in p:
                if c != max(0,h-abs(x-a)-abs(y-b)):
                    flag = 0
                    break
            if flag == 1:
                print(x,y,h)
                exit(0)
if __name__ == '__main__':
    main()
