MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n = int(input())
    if n == 1:
        print('Hello World')
    else:
        a = int(input())
        b = int(input())
        print(a + b)
if __name__ =='__main__':
    main()   
