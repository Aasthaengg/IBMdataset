from math import ceil

N,K = map(int,input().split())
A = sorted([int(i) for i in input().split()]) # 消化コスト
F = sorted([int(i) for i in input().split()],reverse = True) # 食べにくさ
cost = [a*f for a,f in zip(A,F)]

# にぶたん
# K回以下の修行でチーム成績がMになるか
# Mを固定して考える
def grade_is(M:int):
    training = 0
    for i in range(N):
        if cost[i] > M:
            training += ceil((cost[i] - M) / F[i])
        if training > K:
            return False
    return True

def main():
    ok = 10 ** 18 + 1
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if grade_is(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

if __name__ == "__main__":
    main()