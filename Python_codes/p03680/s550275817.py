import sys
n = int(input())
a = [int(input()) for i in range(n)]
x = 0
cnt = 0
l = [False] * n
while x != 1:
    l[x] = True
    x = a[x]-1
    cnt += 1
    if l[x]:
        print(-1)
        sys.exit()
print(cnt)