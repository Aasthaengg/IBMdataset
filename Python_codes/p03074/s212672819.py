n, k = map(int, input().split())
s = input()
lst = []
bef = s[0]
if bef == "0":
    lst.append(0)
cnt = 0
for ss in s:
    if bef == ss:
        cnt += 1
    else:
        lst.append(cnt)
        cnt = 1
        bef = ss
lst.append(cnt)
if s[-1] == "0":
    lst.append(0)

l = len(lst)
if l <= k * 2 + 1:
    print(n)
    exit()
tmp = sum(lst[:2 * k + 1])
ans = tmp
d = 2 * k + 1
for i in range(2 * k + 1, l, 2):
    tmp -= lst[i - d] + lst[i - d + 1]
    tmp += lst[i] + lst[i + 1]
    ans = max(ans, tmp)
print(ans)