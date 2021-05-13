# D
n, k = map(int, input().split())
s = list(input())
count = 0
lr = 0
rl = 0
for i in range(n - 1):
    if s[i] == "L":
        if s[i + 1] == "R":
            # LR
            lr += 1
        else:
            # LL 幸せ
            count += 1
    elif s[i + 1] == "L":
        # RL
        rl += 1
    else:
        # RR 幸せ
        count += 1
#LR,RLのどちらかが内側か判定(外側は見ていないので大きいのが内側)
a = max(rl, lr)
#内側の二倍が幸せになる人数
count += 2 * min(k, a)
#幸せになる人はn人にはならないのでn-1と最小をとる
print(min(count,n-1))