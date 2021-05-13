import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
s = input()
t = input()
val = max(i for i in range(n+1) if i==0 or s[-(i):]==t[:i])
ans = 2*n - val
print(ans)