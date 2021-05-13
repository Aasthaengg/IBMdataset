n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))

M = max(t)
t = [t[0]-1] + t + [t[-1]+1]
a = [a[0]-1] + a + [a[-1]+1]

flag = True
count = 1
for i in range(n):
    if t[i+1] == M and a[i+1] == M:
        flag = False
        if t[i] == M and a[i] == M and t[i+2] == M and a[i+2] == M:
            count = (count * t[i+1]) % (10**9+7)
        continue
    if flag:
        if t[i+1] == t[i]:
            count = (count * t[i+1]) % (10**9+7)
    else:
        if a[i+1] == a[i+2]:
            count = (count * a[i+1]) % (10**9+7)

if flag:
    print(0)
else:
    print(count)