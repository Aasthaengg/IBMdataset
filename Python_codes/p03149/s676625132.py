n = list(map(int, input().split()))
f = [False] * 10

for i in n:
    f[i] = True

if f[1] and f[4] and f[7] and f[9]:
    print("YES")
else:
    print("NO")
