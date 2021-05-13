#coding:utf-8
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = False
def main(given = sys.stdin.readline):
    input = lambda : given().rstrip()
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())
    XLMIIS = lambda x : [LMIIS() for _ in range(x)]
    INF = 10**9


    N,M = LMIIS()
    keys = []
    for i in range(M):
        a,b = LMIIS()
        boxes = map(lambda x: int(x)-1, input().split())
        key = 0
        for b in boxes:
            key += 2**b
        keys.append((a,key))
        



    # 開けられる箱のパターン -> コスト
    dp = [INF] * 2 ** N
    dp[0] = 0

    for key_cost,key in keys:
        for box,cost in enumerate(dp):
            if cost != INF:
                dp[box|key] = min(dp[box|key], cost+key_cost)
    
    ans = dp[2**N-1]
    print(ans if ans != INF else -1)




    




if __name__ == '__main__':
    main()