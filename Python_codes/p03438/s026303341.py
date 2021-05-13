MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = [i - j for i,j in zip(a,b)]
    
    p = 0
    m = 0
    for num in x:
        if num < 0:
            m += (-num//2) * 2
        else:
            p += num
    
    if 2 * p <= m:
        print('Yes')
    else:
        print('No')

if __name__ =='__main__':
    main() 