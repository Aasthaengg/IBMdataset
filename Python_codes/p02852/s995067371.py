n,m = map(int, input().split())
s = input()
s = s[::-1]
ans = list()
goal = False
now = 0
while not goal:
    for adv in reversed(range(1,m+1)):
        if now + adv >= n:
            ans.append(n-now)
            goal = True
            break
        elif s[now+adv] == '0':
            ans.append(adv)
            now += adv
            break
    else:
        print(-1)
        break

if goal:
    print(*ans[::-1])


