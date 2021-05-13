N = int(input())
Score = [0] + [int(input()) for _ in range(N)]
Score.sort()
ans = sum(Score)
flag = True
for s in Score:
    ans -= s
    if ans % 10 != 0:
        flag = False
        break
    else:
        ans += s

if flag:
    print(0)
else:
    print(ans)