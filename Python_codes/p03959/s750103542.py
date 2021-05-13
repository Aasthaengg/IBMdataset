import sys
input = sys.stdin.buffer.readline

n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10**9+7

if n == 1:
    if t[0] != a[0]:
        print(0)
    else:
        print(1)
    exit()

max_list = [10**9+1] * n
min_list = [0] * n

max_list[0] = t[0]
min_list[0] = t[0]
for i in range(1, n):
    if t[i] > t[i-1]:
        max_list[i] = t[i]
        min_list[i] = t[i]
    else:
        max_list[i] = t[i]
        min_list[i] = 1

max_list[n-1] = a[n-1]
min_list[n-1] = a[n-1]
for i in range(n-2, -1, -1):
    if a[i] > a[i+1]:
        if min_list[i] <= a[i] <= max_list[i]:
            max_list[i] = a[i]
            min_list[i] = a[i]
        else:
            print(0)
            exit()
    else:
        if max_list[i] == min_list[i]:
            if max_list[i] > a[i]:
                print(0)
                exit()
        else:
            max_list[i] = min(max_list[i], a[i])

ans = 1
for i in range(n):
    ans = (ans * (max_list[i] - min_list[i] + 1)) % mod
print(ans)
