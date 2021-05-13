n = int(input())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))
k = sum(blst) - sum(alst)
cnt = 0
for a, b in zip(alst, blst):
    cnt += max(0, (b - a + 1) // 2)
if cnt <= k:
    print("Yes")
else:
    print("No")