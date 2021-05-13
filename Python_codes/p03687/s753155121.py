s = input()
n = len(s)

# 求めなくてはいけないアルファベットは、sに含まれているものだけ
abc_kind = set(s)
ans = n
for x in abc_kind:
    # 何も考えず、シミュレーションする
    # xを残すように操作していく
    cnt = 0
    t = s
    while len(t) != t.count(x):
        t = ''.join([x if x in (a, b) else a for a, b in zip(t, t[1:])])
        cnt += 1
    if cnt < ans:
        ans = cnt
print(ans)