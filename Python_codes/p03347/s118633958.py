n = int(input())
a = [int(input()) for i in range(n)]
t = -1
s = 0
ans = 0
for i in range(n):
    if a[i] == t+1:
        t += 1
        s = t
    elif a[i] > t+1:
        print(-1)
        exit()
    else:
        ans += s
        t = a[i]
        s = t
ans += s
print(ans)
