S = input()
b_cnt = 0
ans = 0
for s in S:
    if s == "B":
        b_cnt += 1
    else:
        ans += b_cnt

print(ans)
