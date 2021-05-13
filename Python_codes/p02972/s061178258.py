N = int(input())
a = list(map(int, input().split()))

hako = [0]*N
last_ans = 1

for i in range(N-1, -1, -1):
    #print(i)
    check = 0
    kijun = i+1
    baisuu = 1
    total = 0
    while kijun*baisuu <= N:
        if hako[kijun*baisuu-1] == 1:
            total += 1
        baisuu += 1
    total %= 2
    if total != a[i]:
        hako[i] = 1

if last_ans == 1:
    print(hako.count(1))
    if hako.count(1) != 0:
        buf = [i+1 for i, x in enumerate(hako) if x == 1]
        print(' '.join(map(str, buf)))
else:
    print(-1)