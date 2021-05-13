import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
ans = 1
M = 10**9+7
s = [0,0,0]
for i,num in enumerate(a):
    if num not in s:
        ans = 0
        break
    ans *= sum(item==num for item in s)
    ans %= M
    s[s.index(num)] += 1
print(ans)