import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
v = 0
for num in a:
    v ^= num
if v==0:
    ans = "Yes"
else:
    ans = "No"
print(ans)