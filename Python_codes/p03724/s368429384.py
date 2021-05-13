n, m = map(int, input().split())
p = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    p[a - 1] += 1
    p[b - 1] += 1
flag = True
for i in range(n):
    if p[i] % 2 == 1:
        flag = False
        break
if flag == True:
    print("YES")
else:
    print("NO")