import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

s = input()
n = len(s)
last = []
ans = 0
i = 0
last = []
while i<n:
    if last and s[i]!=last[-1]:
        ans += 2
        last.pop()
        i += 1
    else:
        last.append(s[i])
        i += 1
print(ans)