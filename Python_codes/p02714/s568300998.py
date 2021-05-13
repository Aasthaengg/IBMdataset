import sys

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))


n = ri()
s = rr()
ans = s.count('R') * s.count('G') * s.count('B')
for i in range(n-2):
    for j in range(i+1, n-1):
        k = j + j - i
        if k < n:
            if s[k] != s[j] and s[j] != s[i] and s[k] != s[i]:
                ans -= 1
print(ans)






