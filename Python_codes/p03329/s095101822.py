import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
ans = float("inf")
def sub(x, base):
    if x==0:
        return 0
    i = 0
    while pow(base, i+1)<=x:
        i += 1
    return sub(x-pow(base,i), base) + 1
for i in range(n+1):
    ans = min(ans, sub(i,6)+sub(n-i,9))
print(ans)