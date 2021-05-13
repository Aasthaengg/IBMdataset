import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
n = len(s)
v = []
i = 0
tmp = []
while i<n:
    if s[i]=="A":
        tmp.append(0)
        i += 1
    elif i<n-1 and s[i]=="B" and s[i+1]=="C":
        tmp.append(1)
        i += 2
    else:
        i += 1
        if tmp:
            v.append(tmp)
        tmp = []
if tmp:
    v.append(tmp)
ans = 0
for l in v:
    val = 0
    for c in l:
        if c==1:
            ans += val
        else:
            val += 1
print(ans)