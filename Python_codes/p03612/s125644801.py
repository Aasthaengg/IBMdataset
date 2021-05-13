import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7



def main():
    N = int(readline())
    P = list(map(int, readline().split()))
    for i in range(1,N+1):
        P[i-1] -= i
    P = P + [1,1]
    ans = 0
    i = 0
    while i<N:
        if P[i]==0 and P[i+1]==0:
            ans += 1
            i += 2
        elif P[i]==0 and P[i+1]!=0:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)



if __name__ == '__main__':
    main()