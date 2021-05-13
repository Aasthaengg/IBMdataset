import math

takahashi_hp, t_atack, aoki_hp, a_attack = map(int, input().split())

t_atk_count = aoki_hp / t_atack
a_atk_count = takahashi_hp / a_attack

if math.ceil(a_atk_count) >= math.ceil(t_atk_count):
    print('Yes')
else:
    print('No')
