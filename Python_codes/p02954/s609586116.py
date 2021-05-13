import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
n = len(s)
def run_length(s):
    if not s:
        return []
    c = s[0]
    v = 1
    n = len(s)
    l = []
    for i in range(1, n):
        if c==s[i]:
            v += 1
        else:
            l.append((c,v))
            c = s[i]
            v = 1
    l.append((c,v))
    return l
l = run_length(s)
ans = []
while l:
    ll,rr = l.pop()[1], l.pop()[1]
    tmp = [0]*(rr+ll)
    tmp[rr-1] = (rr-1)//2 + (ll)//2 + 1
    tmp[rr] = rr+ll - tmp[rr-1]
    ans.append(tmp)
res = []
for i in range(len(ans)-1, -1, -1):
    res.extend(ans[i])
write(" ".join(map(str, res)))