n = int(input())
p = list(map(int,input().split()))

m = [False] * n
for i in range(n):
    if p[i] == i+1:
        m[i] = True

ans = 0
flag = False
for i in range(n):
    if flag:
        flag = False
        continue
    if m[i]:
        flag = True
        ans += 1
print(ans)