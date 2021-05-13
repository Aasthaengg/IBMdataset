import sys
n = int(input())
a = list(map(int,input().split()))

flag = False
b = []
cnt = 1
for i in range(n):
    if a[i] == cnt:
        flag = True
        b += [i]
        cnt += 1

if not flag:
    print(-1)
    sys.exit()

print(n - len(b))