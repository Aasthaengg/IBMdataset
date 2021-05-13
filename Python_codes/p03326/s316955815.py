import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N,M = map(int,input().split())
    cake = [tuple(map(int,input().split())) for _ in range(N)]
    
    ans = 0
    for bit in range(1<<3):
        op = [-1] * 3
        for i in range(3):
            if (bit>>i)&1:
                op[i] = 1
        cake.sort(key = lambda x:x[0]*op[0] + x[1]*op[1] + x[2]*op[2],reverse=True)
        ans = max(ans,sum(op[0]*c[0] + op[1]*c[1] + op[2]*c[2] for c in cake[:M]))
    print(ans)

if __name__ == '__main__':
    main()