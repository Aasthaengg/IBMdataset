n = int(input())
goal = list(map(int,input().split()))
now = [0]*n
ans = 0

while goal != now:
    x = 0
    for i in range(n):
        if x == 0 and now[i] != goal[i]:
            x = 1
            now[i] += 1
        elif x == 1 and now[i] != goal[i]:
            now[i] += 1
        elif x == 1 and now[i] == goal[i]:
            break
    ans += 1

print(ans)
