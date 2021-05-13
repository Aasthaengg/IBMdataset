n = int(input())
p = list(map(int,input().split()))
ans = 0

flag = False
for i in range(n):
    if flag:
        flag = False
        continue
    if p[i] == i+1:
        if i < n-1 and p[i+1] == i+2:
            flag = True
        ans += 1

print(ans)
