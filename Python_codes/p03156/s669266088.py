n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in p:
    if i <= a:
        cnt1 += 1
    elif i <= b:
        cnt2 += 1
    else:
        cnt3 += 1
ans = min(cnt1, cnt2, cnt3)
print(ans)