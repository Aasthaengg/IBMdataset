import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))

a.sort()
mc = sum(item<0 for item in a)
ans = []
if mc==1 or mc==0:
    val = a[0]
    for i in range(n-2):
        ans.append((val, a[i+1]))
        val = val - a[i+1]
    ans.append((a[n-1], val))
    value = a[n-1] - val
elif mc<n:
    val = a[-1]
    for i in range(mc-1):
        ans.append((val, a[i]))
        val -= a[i]
    val2 = a[mc-1]
    for i in range(mc, n-1):
        ans.append((val2, a[i]))
        val2 -= a[i]
    ans.append((val, val2))
    value = val-val2
else:
    val = a[-1]
    for i in range(n-1):
        ans.append((val, a[i]))
        val -= a[i]
    value = val
        
print(value)
write("\n".join(" ".join(map(str, item)) for item in ans))