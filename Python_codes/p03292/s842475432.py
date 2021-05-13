import sys
sys.setrecursionlimit(100000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    A = list(map(int,input().split()))
    ret = abs(A[0] - A[1]) + abs(A[1] - A[2]) + abs(A[2] - A[0])
    ans = INF
    for i in range(3):
        ans = min(ans,ret - abs(A[i] - A[(i+1)%3]))
    print(ans)

if __name__ == '__main__':
    main()

