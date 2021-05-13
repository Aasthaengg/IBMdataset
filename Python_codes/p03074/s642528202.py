n, k = map(int,input().split())
s = input()

ns = []
now_num = s[0]
cnt = 0
for i in range(n):
    if now_num == s[i]:
        cnt += 1
    else:
        ns.append((now_num, cnt))
        now_num = s[i]
        cnt = 1
ns.append((now_num, cnt))
len_ns = len(ns)
pre = [0] * (len_ns + 1)
for i in range(len_ns):
    pre[i + 1] = pre[i] + ns[i][1]

ans = 1
for i in range(len_ns - 2*k + 1):
    temp = pre[i + 2*k] - pre[i]
    if i > 0 and ns[i - 1][0] == '1':temp += ns[i - 1][1]
    if i + 2*k < len_ns and ns[i + 2*k][0] == '1':temp += ns[i + 2*k][1]
    if temp > ans:ans = temp
print(ans if len_ns - 2*k + 1 > 0 else len(s))