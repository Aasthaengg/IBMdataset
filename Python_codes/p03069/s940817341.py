import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
s = readline().rstrip().decode('utf-8')
res = s.count(".")
ans = res
for i in range(n):
    if s[i] == "#":
        res += 1
    else:
        res -= 1
    ans = min(ans,res)

print(ans)