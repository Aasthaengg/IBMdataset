n = int(input())
a, b = map(int, input().split())
ls = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in range(n):
    if ls[i] <= a:
        cnt1 += 1
    elif a + 1 <= ls[i] <= b:
        cnt2 += 1
    elif ls[i] >= b + 1:
        cnt3 += 1

print(min(cnt1, cnt2, cnt3))