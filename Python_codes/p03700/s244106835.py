N, A, B = map(int, input().split())
h = []
for _ in range(N):
    h.append(int(input()))

sum_h = sum(h)
sum_dam = B * N + (A - B)
ng = (sum_h - 1) // sum_dam + 1 - 1
ok = (max(h) - 1) // B + 1
ans = (ng + ok + 1) // 2
while ok - ng > 1:
    cnt = ans
    flag = 0
    for h_i in h:
        rem = h_i - B * ans
        if rem > 0:
            cnt -= (rem - 1) // (A - B) + 1
            if cnt < 0:
                flag = 1
                break
    if flag == 0:
        ok = ans
    else:
        ng = ans
    ans = (ng + ok + 1) // 2

print(ans)
