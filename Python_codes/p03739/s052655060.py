n = int(input())
A = list(map(int, input().split()))

# pattern1
goukei = 0
ans1 = 0
for i in range(n):
    goukei += A[i]
    if i % 2:
        if goukei >= 0:
            ans1 += goukei + 1
            goukei = -1
    else:
        if goukei <= 0:
            ans1 += 1 - goukei
            goukei = 1
# pattern2
goukei = 0
ans2 = 0
for i in range(n):
    goukei += A[i]
    if i % 2:
        if goukei <= 0:
            ans2 += 1 - goukei
            goukei = 1
    else:
        if goukei >= 0:
            ans2 += goukei + 1
            goukei = -1
print(min(ans1, ans2))
