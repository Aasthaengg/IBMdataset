N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

cnt1, cnt2, cnt3 = 0, 0, 0
for i in range(N):
    if P[i] <= A:
        cnt1 += 1
    elif A < P[i] <= B:
        cnt2 += 1
    else:
        cnt3 += 1
print(min(cnt1, cnt2, cnt3))
