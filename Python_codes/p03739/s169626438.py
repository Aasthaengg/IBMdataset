n = int(input())
a = list(map(int,input().split()))

S1 = 0
S2 = 0
#S1が奇数番目が正の場合、S2が偶数番目が負の場合
cnt1 = 0
cnt2 = 0

for i,num in enumerate(a):
    S1 += num
    if i % 2 == 0 and S1 <= 0:
        cnt1 += 1 - S1
        S1 = 1
    if i % 2 != 0 and S1 >= 0:
        cnt1 += 1 + S1
        S1 = -1

    S2 += num
    if i % 2 == 0 and S2 >= 0:
        cnt2 += 1 + S2
        S2 = -1
    if i % 2 != 0 and S2 <= 0:
        cnt2 += 1 - S2
        S2 = 1

print(cnt1 if cnt1 <= cnt2 else cnt2)
