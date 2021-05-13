N = int(input())
A = list(map(int, input().split()))

c = A[0]
ans1 = 0
for a in A[1:]:
    if c > 0 and c + a >= 0:
        ans1 += c + a + 1
        c = -1

    elif c < 0 and c + a <= 0:
        ans1 += -(c + a) + 1
        c = 1

    else:
        c = c + a


c = 1
ans2 = abs(A[0] - 1)
for a in A[1:]:
    if c > 0 and c + a >= 0:
        ans2 += c + a + 1
        c = -1

    elif c < 0 and c + a <= 0:
        ans2 += -(c + a) + 1
        c = 1

    else:
        c = c + a


c = -1
ans3 = abs(A[0] + 1)
for a in A[1:]:
    if c > 0 and c + a >= 0:
        ans3 += c + a + 1
        c = -1

    elif c < 0 and c + a <= 0:
        ans3 += -(c + a) + 1
        c = 1

    else:
        c = c + a

print(min(ans1, ans2, ans3))
