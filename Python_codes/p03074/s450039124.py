import itertools
N, K = map(int, input().split())
S = input()
flg = int(S[0])
gr = itertools.groupby(S)
ans, tmp = 0, 0
check_0, check_1 = [], []
for key, group in gr:
    target = len(list(group))
    tmp += target
    if key == '1':
        check_1.append(target)
    else:
        check_0.append(target)
    if key == '0':
        if len(check_0) > K:
                tmp -= check_0[len(check_0)-(K+1)]
        if len(check_1) > K:
                tmp -= check_1[len(check_1)-(K+1)]
    ans = max(ans,tmp)
print(ans)