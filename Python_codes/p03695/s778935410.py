N = int(input())
A = list(map(int, input().split()))

ans = [0]*8
leng = 0

for i in range(N):
    if 1 <= A[i] <= 399:
        ans[0] = 1
    elif 400 <= A[i] <= 799:
        ans[1] = 1
    elif 800 <= A[i] <= 1199:
        ans[2] = 1
    elif 1200 <= A[i] <= 1599:
        ans[3] = 1
    elif 1600 <= A[i] <= 1999:
        ans[4] = 1
    elif 2000 <= A[i] <= 2399:
        ans[5] = 1
    elif 2400 <= A[i] <= 2799:
        ans[6] = 1
    elif 2800 <= A[i] <= 3199:
        ans[7] = 1
    else:
        leng += 1

mi = sum(ans) if sum(ans) > 0 else 1
print(mi, sum(ans) + leng)
