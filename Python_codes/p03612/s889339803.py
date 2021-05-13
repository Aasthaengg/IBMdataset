n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(n):
    if p[i] == i+1:
        ans += 1
        now = i
        to = i
        if i == 0:
            to = i + 1
        elif i == n-1:
            to = i - 1
        else:
            if p[i-1] == i:
                to = i - 1
            else:
                to = i + 1
        tmp = p[now]
        p[now] = p[to]
        p[to] = tmp
        

print(ans)
