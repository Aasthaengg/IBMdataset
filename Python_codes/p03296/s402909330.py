n = int(input())
a = input().split()
cnt = 0
for i in range(1,n):
    if a[i-1] == a[i]:
        a[i] = -i
        cnt += 1
print(cnt)