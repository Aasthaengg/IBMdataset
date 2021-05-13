import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a = list(map(int, input().split()))
if sum(a)>21:
    ans = "bust"
else:
    ans = "win"
print(ans)