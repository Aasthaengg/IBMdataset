N = int(input())
a = list(map(int, input().split()))

cnt2 = 0  # 2で割り切れる回数
cnt4 = 0  # 4で割り切れる回数

for i in range(N):
    if a[i] % 4 == 0:
        cnt4 += 1
    elif a[i] % 2 == 0:
        cnt2 += 1

if N-max(cnt2-1, 0) <= cnt4*2+1:
    print('Yes')
else:
    print('No')

