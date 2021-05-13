N, K = [int(x) for x in input().split()]
R, S, P = [int(x) for x in input().split()]
T = input()

# 相手に勝つ時に得られる点数
def rsp(hand):  # hand : 相手の手
    if hand == 'r':
        ret = P
    elif hand == 's':
        ret = R
    else:
        ret = S
    return ret

ans = 0
for i in range(K):
    Ti = T[i : : K]
    cnt = 0
    for j in range(len(Ti)):
        if j == 0 or Ti[j] == Ti[j - 1]:
            cnt += 1
        else:
            ans += rsp(Ti[j - 1]) * ((cnt + 1) // 2)
            cnt = 1
    ans += rsp(Ti[-1]) * ((cnt + 1) // 2)

print(ans)