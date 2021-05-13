import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]

# スタート＋
if a[0] <= 0:
    A1 = 1
    ans1 = abs(a[0]) + 1
else:
    A1 = a[0]
    ans1 = 0
for i in range(1, n):
    nextA = A1 + a[i]
    if (A1 > 0 and nextA < 0) or (A1 < 0 and nextA > 0):
        A1 = nextA
    elif nextA == 0 and A1 > 0:
        ans1 += 1
        A1 = -1
    elif nextA == 0 and A1 < 0:
        ans1 += 1
        A1 = 1
    elif A1 > 0:
        ans1 += abs(nextA) + 1
        A1 = -1
    else:
        ans1 += abs(nextA) + 1
        A1 = 1

# スタート-
if a[0] >= 0:
    ans2 = abs(a[0]) + 1
    A2 = -1
else:
    A2 = a[0]
    ans2 = 0
for i in range(1, n):
    nextA = A2 + a[i]
    if (A2 > 0 and nextA < 0) or (A2 < 0 and nextA > 0):
        A2 = nextA
    elif nextA == 0 and A2 > 0:
        ans2 += 1
        A2 = -1
    elif nextA == 0 and A2 < 0:
        ans2 += 1
        A2 = 1
    elif A2 > 0:
        ans2 += abs(nextA) + 1
        A2 = -1
    else:
        ans2 += abs(nextA) + 1
        A2 = 1

print(min(ans1, ans2))


