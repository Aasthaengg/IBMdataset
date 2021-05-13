import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = list(map(int,readline().split()))
ans = 0
flag = 0
for i in range(n-1):
    if flag:
        flag = 0
        continue
    if lst1[i] == lst1[i+1]:
        ans += 1
        flag = 1

print(ans)