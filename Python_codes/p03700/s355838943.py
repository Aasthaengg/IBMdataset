n, a, b = map(int, input().split())
monsters = [int(input()) for _ in range(n)]

right = max(monsters) // b + 1
left = 0

while left+1 < right:
    bomb_count = (left+right) // 2
    base_damage = bomb_count * b

    center_count = 0
    for hp in monsters:
        if hp <= base_damage:
            continue

        remaining_hp = hp - base_damage
        need_center = (remaining_hp + a-b-1) // (a-b)
        center_count += need_center

    if center_count <= bomb_count:
        right = bomb_count
    else:
        left = bomb_count

print(right)
