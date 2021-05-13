import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s,w = list(map(int, input().split()))
if s<=w:
    ans = "unsafe"
else:
    ans = "safe"
print(ans)