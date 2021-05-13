import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
ans = float("inf")
for i in range(1, n):
    a,b = i, n-i
    ans = min(ans, sum(map(int, str(a)))+sum(map(int, str(b))) )
print(ans)