import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
s = input()
### ローリングハッシュ rolling hash
import random
# M = 10**9+7
# M = 1<<63 - 1
M = 92709568269121

b = random.choice(range(1,M))
def rhash_list(s):
    l = [chr(v) for v in range(ord("a"), ord("z")+1)]
    d = {c:i+2 for i,c in enumerate(l)}
    ans = 0
    v = 1
    l = [0]
    for item in s:
        ans += d[item]*v
        v *= b
        ans %= M
        v %= M
        l.append(ans)
    return l
l = rhash_list(s)
if len(set(s))==n:
    ans = 0
else:
    binv = pow(b,M-2,M)
    pows = [None]*(n+1)
    v = 1
    for j in range(n+1):
        pows[j] = v
        v *= binv
        v %= M
#         pow(binv,j,M)
    ans = 0
    from collections import defaultdict
    for i in range(n//2, 0, -1):
        d = defaultdict(list)
        for j in range(n-i+1):
            d[((l[j+i]-l[j])*pows[j])%M].append(j)
        for v in d.values():
            if v[0]+i<=v[-1]:
                ans = i
        if ans>0:
            break
print(ans)