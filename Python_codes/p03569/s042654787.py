s = input()
n = len(s)

s_wo_x = s.replace("x", "")
if s_wo_x != s_wo_x[::-1]:
    print(-1)
else:
    num_x = []
    cnt = 0
    for i in range(n):
        if s[i] == "x":
            cnt += 1
        else:
            num_x.append(cnt)
            cnt = 0
    num_x.append(cnt)

    ans = 0
    N = len(num_x)
    for i in range(N // 2):
        if num_x[i] == num_x[N - i - 1]:
            continue
        else:
            ans += abs(num_x[i] - num_x[N - i - 1])

    if N % 2 == 1:
        if num_x[N // 2] % 2 > 1 and num_x[N // 2] % 2 == 0:
            ans += 1
    print(ans)
