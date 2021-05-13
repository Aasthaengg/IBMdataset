MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n = int(input())
    if n%2 == 0:
        print(n//2,n,n)
        return
    for i in range(1,3501):
        for j in range(i + 1,3501):
            if (n * i * j)%(4 * i * j - n * j - n * i) == 0:
                ans = (i ,j , (n * i * j)//(4 * i * j - n * j - n * i))
                break
    
    print(*ans)

if __name__ =='__main__':
    main()  