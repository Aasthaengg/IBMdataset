import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
c = 1
ans = 0
prev = a[0]
for num in a[1:]:
    if num==prev:
        c += 1
    else:
        ans += (c//2)
        c = 1
    prev = num
ans += (c//2)
print(ans)