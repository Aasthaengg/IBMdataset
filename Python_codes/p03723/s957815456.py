import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


l = list(map(int, input().split()))
l.sort()
a,b,c = l
ans = 0
while True:
    if a%2 or b%2 or c%2:
        break
    if a==b==c:
        ans = -1
        break
    a,b,c = b//2+c//2, a//2+c//2, a//2+b//2
    ans += 1
print(ans)