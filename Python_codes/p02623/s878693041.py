N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Asum_li = [0]
Asum = 0
Bsum_li = [0]
Bsum = 0

for A_ in A:
    Asum = Asum + A_
    Asum_li.append(Asum)

for B_ in B:
    Bsum = Bsum + B_
    Bsum_li.append(Bsum)

cnt_max = 0
cnt_b = M

for cnt_a in range(N+1):

    if Asum_li[cnt_a] > K : break

    while (Bsum_li[cnt_b] + Asum_li[cnt_a]) > K:
        cnt_b = cnt_b - 1
        if cnt_b < 0: break

    if (cnt_max < cnt_a + cnt_b): cnt_max = cnt_a + cnt_b


print(cnt_max)

