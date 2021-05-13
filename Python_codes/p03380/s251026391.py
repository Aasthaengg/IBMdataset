n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans1 = max(A)
if A[1] == 0:
    print(ans1, 0)
for i in range(n):
    if i == 0:
        pass
    elif i == 1:
        ans2 = A[i]
        now_div = abs(ans1/2 - ans2)
    else:
        chk = A[i]
        chk_div = abs(ans1/2 - chk)
        if chk_div > now_div:
            print(ans1, ans2)
            exit()
        if abs(ans1/2 - chk) < abs(ans1/2 - ans2):
            ans2 = chk
            now_div = abs(ans1/2 - ans2)