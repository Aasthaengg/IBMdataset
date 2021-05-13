import math
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum_A = sum(A)
sum_B = sum(B)
cnt1 = sum_B - sum_A
cnt2 = 0
for a, b in zip(A, B):
    # if a > b:
    #     cnt2 += a - b
    if a < b:
        cnt2 += math.ceil((b - a) / 2)

if cnt1 >= cnt2:
    print("Yes")
else:
    print("No")