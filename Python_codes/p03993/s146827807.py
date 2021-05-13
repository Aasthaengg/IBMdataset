N = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if a[i] == -1:
        pass
    else:
        if a[a[i]-1] == i+1:
            cnt += 1
            a[a[i]-1] = -1
print(cnt)