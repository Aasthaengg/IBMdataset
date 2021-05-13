n, k, c = map(int, input().split())
s = input()
l = [-1] * n
r = [-1] * n
pre = -n - 1
cnt = 0
for i in range(0, n):
    if s[i] == 'x':
        continue
    if i - pre - 1 >= c:
        l[cnt] = i + 1
        cnt += 1
        pre = i
cnt = 0
pre = 2 * n + 1
for i in range(n - 1, -1, -1):
    if s[i] == 'x':
        continue
    if pre - i - 1 >= c:
        
        r[k - cnt - 1] = i + 1
        cnt += 1
        pre = i
ans = []
for i in range(0, k):
    if l[i] == r[i] and l[i] != -1:
        ans.append(l[i])
for x in ans:
    print(x)