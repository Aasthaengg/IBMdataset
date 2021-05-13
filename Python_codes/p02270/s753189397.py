import sys
input=sys.stdin.readline
import math

#input = open(sys.argv[1], "r").readline

def main():
    N,K = map(int,input().split())
    W = []
    for _ in range(N):
        W.append(int(input()))

    # (lb, ub] の間を二分探索
    lb = max(W)-1   # 最大の w さえ積めれば良い場合が p の取り得る最小値
    ub = sum(W)     # 全てを 1 台のトラックに積む必要がある場合が p の取り得る最大値

    while ub - lb > 1:
        p = (lb + ub)//2

        v = 0
        k = 1
        for w in W:
            if v + w <= p: # 積載オーバーしなければ積む
                v += w
            else:
                k += 1
                v = w

        if k <= K:
            # p が条件を満たしている ⇒ 解の存在範囲を (lb, p] に更新
            ub = p
        else:
            # p が条件を満たしていない ⇒ 解の存在範囲を (p, ub] に更新
            lb = p
#        print(p,k,lb,ub)

    # この時点で lb + 1 = ub となっている
    print(ub)

if __name__ == '__main__':
    main()

