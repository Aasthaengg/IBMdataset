N = int(input())
monster = list(map(int, input().split()))
hero = list(map(int, input().split()))
ans = 0

for i in range(N):
    i1_enemy = monster[i]
    i2_enemy = monster[i+1]
    atk = hero[i]
    if atk <= i1_enemy:
        ans += atk
    elif i1_enemy <= atk <= i1_enemy + i2_enemy:
        ans += atk
        monster[i+1] = i1_enemy + i2_enemy - atk
    else:
        ans += i1_enemy + i2_enemy
        monster[i+1] = 0

print(ans)


