import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

abc = list(map(int, readline().split()))
abc.sort()

ans = abc[2]-abc[1]
res = abc[1]-abc[0]
if res % 2 == 0:
    ans += res // 2
else:
    ans += res // 2 + 2

print(ans)