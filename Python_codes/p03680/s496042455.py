N = int(input())
used = [False]*(N+1)
used[1] = True
a = [None]*(N+1)
for i in range(1,N+1):
    x = int(input())
    a[i] = x
x = a[1]
cnt = 1
while True:
    if used[x] == True:
        print(-1)
        break
    if x == 2:
        print(cnt)
        break
    used[x] = True
    x = a[x]
    cnt += 1
