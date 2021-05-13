#coding:utf-8
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = False
def main(input = sys.stdin.readline):
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())

    N,M = LMIIS()
    for i in range(M//N,0,-1):
        if M % i == 0:
            print(i)
            return



if __name__ == '__main__':
    main()