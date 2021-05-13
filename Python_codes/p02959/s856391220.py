n = int(input())
enemy  = list(map(int,input().split()))
hero  = list(map(int,input().split()))

ans = 0

for i in range(n):
    if hero[i] > enemy[i]:
        if enemy[i+1] < (hero[i]-enemy[i]):
            ans += (enemy[i]+enemy[i+1])
            enemy[i+1] = 0
        else:
            enemy[i+1] -= (hero[i]-enemy[i])
            ans += hero[i]
    else:
        ans += hero[i]

print(ans)