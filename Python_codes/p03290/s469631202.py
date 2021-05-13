# C - All Green

D, G = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(D)]

ans = 10**18
for i in range(1<<D):
    tmp = 0
    cnt = 0
    for j in range(D):
        if (i>>j)&1:
            p, c = P[j]
            tmp += p * (j+1) * 100 + c
            cnt += p
    if tmp >= G:
        ans = min(ans, cnt)
    else:
        xor_i = i^((1<<D)-1)
        for k in range(D)[::-1]:
            if (xor_i)>>k&1:
                p, c = P[k]
                for _ in range(p):
                    tmp += (k+1) * 100
                    cnt += 1
                    if tmp >= G:
                        ans = min(ans, cnt)
                        break
                else:
                    break
                break

print(ans)
