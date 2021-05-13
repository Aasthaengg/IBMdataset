import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
i = 0
j = len(s)-1
ans = 0
while i<=j:
    if s[i]!=s[j]:
        ans += 1
    i += 1
    j -= 1
print(ans)