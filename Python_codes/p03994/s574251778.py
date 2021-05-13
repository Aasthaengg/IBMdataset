from sys import stdin
import string
s = (stdin.readline().rstrip())
K = int(stdin.readline().rstrip())

alp = string.ascii_lowercase*3
ans = ""
for i in s:
    ind = alp.index(i)
    cnt = 0
    if i == "a":
        ans += "a"
        continue
    for j in alp[ind+1:]:
        cnt += 1
        if K - cnt < 0:
            ans += i
            cnt = 0
            break
        if j == "a":
            ans += "a"
            K = K - cnt
            cnt = 0
            break
if K != 0:
    ind = (K % 26) + alp.index(ans[-1])
    ans = ans[:-1]+alp[ind]
print(ans)