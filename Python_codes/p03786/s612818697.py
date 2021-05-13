import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
a.sort()
def sub(x):
    v = a[x]
    for i,num in enumerate(a):
        if i==x:
            continue
        if v*2>=num:
            v += num
        else:
            ans = False
            break
    else:
        ans = True
    return ans
if sub(0):
    ans = n
elif not sub(n-1):
    ans = 0
else:
    l = 0
    r = n
    while l<r-1:
        m = (l+r)//2
        if sub(m):
            r = m
        else:
            l = m
    ans = n-r
print(ans)