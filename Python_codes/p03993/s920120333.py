n = int(input())
a = list(map(int,input().split()))
cnt = 0
tmp = 0
for i in range(n):
    tmp = a[i] - 1
    if a[tmp] == i + 1:
        cnt += 1
print(cnt//2)