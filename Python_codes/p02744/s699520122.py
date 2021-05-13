n = int(input())
import copy
ans = [[0]]
for i in range(n-1):
    x = len(ans)
    for j in range(x):
        mx = max(ans[j])
        for k in range(mx+2):
            tmp = ans[j].copy()
            tmp.append(k)
            ans.append(tmp)
    ans = [s for s in ans if len(s)==i+2]
for s in ans:
    tmp = ""
    for i in s:
        tmp += chr(ord("a")+ i)
    print(tmp)