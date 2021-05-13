N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
rsp = [set() for i in range(3)]
ans = 0
for i in range(N):
    if T[i] == 'r' and i - K not in rsp[0]:
        ans += P
        rsp[0].add(i)
    elif T[i] == 's' and i - K not in rsp[1]:
        ans += R
        rsp[1].add(i)
    elif T[i] == 'p' and i - K not in rsp[2]:
        ans += S
        rsp[2].add(i)
print(ans)
