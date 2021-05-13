N, Q = map(int, input().split())
S = input()
qn = [list(map(int, input().split())) for _ in range(Q)]
S = "0" + S
cnt = []
cnt.append(0)
for i in range(1, N+1):
    if (S[i-1:i+1] == "AC"):
        cnt.append(cnt[i-1] + 1)
    else:
        cnt.append(cnt[i-1])
for q in qn:
    ans = cnt[q[1]] - cnt[q[0]-1]
    if S[q[0]-1:q[0]+1] == "AC":
        ans -= 1
    print(ans)