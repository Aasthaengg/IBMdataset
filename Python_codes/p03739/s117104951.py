n = int(input())
A = list(map(int, input().split()))
A2 = A[:]
RAW = A[:]

# +-にするとき
su = 0
for i, a in enumerate(A):
    su += a
    if i % 2 == 0:
        if su <= 0:
            # a[i] を増やす
            t = (-su + 1)
            A[i] += t
            su += t
    else:
        if su >= 0:
            # a[i] をへらす
            t = (su + 1)
            A[i] -= t
            su -= t

# -+にするとき
su = 0
for i, a in enumerate(A2):
    su += a
    t = 0
    if i % 2 ==0:
        if su >= 0:
            # a[i]をへらす
            t = (su + 1)
            A2[i] -= t
            su -= t
    else:
        if su <= 0:
            # a[i]をふやす
            t = (-su + 1)
            A2[i] += t
            su += t
# print(A)
# print(A2)

ans1 = sum([abs(a-b) for a,b in zip(A, RAW)])
ans2 = sum([abs(a-b) for a,b in zip(A2, RAW)])
print(min(ans1, ans2))