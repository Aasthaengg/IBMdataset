# 2020/05/06
# AtCoder Grand Contest 009 - A

# Input
n = int(input())

cnt = 0
ablist = list()
for i in range(n):
    ab = list(map(int,input().split()))
    ablist.append(ab)

# Calc from Last element
for i in range(n-1, -1, -1):
    rem = (ablist[i][0] + cnt) % ablist[i][1]
    if rem > 0:
        addval = ablist[i][1] - rem
        cnt = cnt + addval

# Output
print(cnt)
