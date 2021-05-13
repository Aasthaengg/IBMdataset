t_hp, t_atk, a_hp, a_atk = map(int, input().split())

while True:
    a_hp = a_hp - t_atk
    if a_hp <= 0:
        print('Yes')
        break
    t_hp = t_hp - a_atk
    if t_hp <= 0:
        print('No')
        break