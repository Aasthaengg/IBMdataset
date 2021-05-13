n, k = map(int, input().split())
s = input()
right = s.count("R")
left = s.count("L")

if min(right, left) <= k:
    print(n-1)
elif n == 1:
    print(0)
else:
    # 操作前の幸福な人の数を調べる
    happy = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            happy += 1
    #print(happy)
    # RL...LR,LR...RLを数える
    rl = s.count("RL")
    lr = s.count("LR")
    #print(rl, lr)
    min_rllr = min(rl, lr)
    max_rllr = max(rl, lr)
    if rl != 0 and lr != 0:
        if k > min_rllr:
            happy += min_rllr*2 + (max_rllr-min_rllr)
        else:
            happy += k*2
    else:
        happy += k
    print(happy)
