import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = list(map(int, input()))
ans = sum(n)
s = 0
for i,num in enumerate(n):
    if num>=1:
        ans = max(ans, s + (num-1) + 9*(len(n)-i-1))
    s += num
print(ans)