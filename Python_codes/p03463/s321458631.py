import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,a,b = list(map(int, input().split()))
dif = b-a-1
if dif%2==0:
    ans = "Borys"
else:
    ans = "Alice"
print(ans)