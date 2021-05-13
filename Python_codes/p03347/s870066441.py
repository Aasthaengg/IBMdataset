import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int,read().split()))

if(a[0] != 0):
    print(-1)
    exit()

if(n==1):
    print(0)
    exit()

ans = a[-1]
for i in range(n-2,-1,-1):
    if(a[i+1] - a[i] == 1):
        continue
    elif(a[i+1] - a[i] > 1):
        print(-1)
        exit()
    ans += a[i]

print(ans)