import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
# if any(item%2==1 for item in a):
if not all(item%2==0 for item in a):
    ans = "first"
else:
    ans = "second"
print(ans)