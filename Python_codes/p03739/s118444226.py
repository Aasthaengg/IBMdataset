n = int(input())

a = list(map(int, input().split()))

total = 0
ans_m = 0
ans_p = 0

hugo = 1
for i in range(n):
    total += a[i]
    if hugo == -1 and total <= 0:
        ans_p = ans_p + (1-total)
        total = 1
        hugo = 1
    elif hugo == -1 and total > 0:
        hugo = 1
    elif hugo == 1 and total >= 0:
        ans_p = ans_p + (1+total)
        total = -1
        hugo = -1
    elif hugo == 1 and total < 0:
        hugo = -1

total = 0
hugo = -1

for i in range(n):
    total += a[i]
    if hugo == -1 and total <= 0:
        ans_m = ans_m + (1-total)
        total = 1
        hugo = 1
    elif hugo == -1 and total > 0:
        hugo = 1
    elif hugo == 1 and total >= 0:
        ans_m = ans_m + (1+total)
        total = -1
        hugo = -1
    elif hugo == 1 and total < 0:
        hugo = -1

print(min(ans_m, ans_p))