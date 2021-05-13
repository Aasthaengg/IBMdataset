import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = [a[i]-b[i] for i in range(n)]
l.sort()
if sum(l)<0:
    ans = -1
else:
    s = sum(l[i] for i in range(n) if l[i]<0)
    if s>=0:
        ans = 0
    else:
        for j in range(n-1, -1, -1):
            s += l[j]
            if s>=0:
                break
        ans = sum(l[i]<0 for i in range(n)) + (n-j)
print(ans)