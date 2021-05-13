import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

cnt = 0
flag = 0

for i in range(n - 1):
    if flag == 0:
        if a[i + 1] - a[i] > 0:
            flag = 1
        elif a[i + 1] - a[i] < 0:
            flag = -1
    elif flag == 1 and a[i + 1] - a[i] < 0:
        cnt += 1
        flag = 0
    elif flag == -1 and a[i + 1] - a[i] > 0:
        cnt += 1
        flag = 0
print(cnt + 1)