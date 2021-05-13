# 2020/05/07
# AtCoder Grand Contest 013 - A

# Input
n = int(input())
a = list(map(int,input().split()))

# Calc
cnt = 1
dr = 0
sav = a[0]
for i in range(1, n):
    # Initial Status
    if dr == 0:
        # Increase
        if sav < a[i]:
            dr = 1
        # Decrease
        elif sav > a[i]:
            dr = -1
    # Case Increase
    elif dr == 1:
        if sav > a[i]:
            cnt = cnt + 1
            dr = 0
    # Case Decrease
    elif dr == -1:
        if sav < a[i]:
            cnt = cnt + 1
            dr = 0
    sav = a[i]

ans = cnt

# Output
print(ans)
