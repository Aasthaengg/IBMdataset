n = int(input())
a = list(map(int, input().split()))
cnt = 0
f = 0
for i in range(1, n):
    if a[i-1] < a[i]:
        ff = 1
    elif a[i-1] > a[i]:
        ff = -1
    else:
        ff = 0
    if f and ff and f != ff:
        cnt += 1
        f = 0
    elif not f:
        f = ff

print(cnt + 1)