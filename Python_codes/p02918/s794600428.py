import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
s = input()
v = 0
l = [[s[0],1]]
for c in s[1:]:
    if l[-1][0]!=c:
        l.append([c,1])
    else:
        l[-1][1] += 1
vs = []
if len(l)==1:
    ans = n-1
else:
    num = 0
    for i in range(n):
        if (i==0 and s[i]=="L") or (i==n-1 and s[i]=="R") or (0<=i<=n-2 and s[i]=="R" and s[i+1]=="L") or (1<=i and s[i]=="L" and s[i-1]=="R"):
            num += 1
    vals = []
    for i in range(len(l)):
        if l[i][0]=="L":
            if i in (0, len(l)-1):
                vals.append(1)
            else:
                vals.append(2)
    vals.sort()
    ans = n - (num - sum(vals[-k:]))
    
    vals = []
    for i in range(len(l)):
        if l[i][0]=="R":
            if i in (0, len(l)-1):
                vals.append(1)
            else:
                vals.append(2)
    vals.sort()
    ans = max(ans, n - (num - sum(vals[-k:])))
    
print(ans)