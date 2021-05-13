N = int(input())
A = tuple(map(int, input().split(' ')))

if A[0] == 0:
    cs = 1
    ans1 = 1
else:
    cs = A[0]
    ans1 = 0

for na in A[1:]:
    if cs >= 0:
        cs += na
        if cs < 0:
            continue

        ans1 += abs(cs) + 1
        cs = -1
    else:
        cs += na
        if cs > 0:
            continue

        ans1 += abs(cs) + 1
        cs = 1

if A[0] == 0:
    cs = -1
    ans2 = 1
elif A[0] > 0:
    cs = -1
    ans2 = abs(A[0]) + 1
else:
    cs = 1
    ans2 = abs(A[0]) + 1

for na in A[1:]:
    if cs >= 0:
        cs += na
        if cs < 0:
            continue

        ans2 += abs(cs) + 1
        cs = -1
    else:
        cs += na
        if cs > 0:
            continue

        ans2 += abs(cs) + 1
        cs = 1

print(min(ans1, ans2))
