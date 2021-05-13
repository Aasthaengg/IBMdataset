import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)

def main():
    n = int(input())
    flag = True
    for _ in range(n):
        a = int(input())
        if a%2 != 0:
            flag = False
            break
    
    if flag:
        print('second')
    else:
        print('first')
if __name__=='__main__':
    main()


