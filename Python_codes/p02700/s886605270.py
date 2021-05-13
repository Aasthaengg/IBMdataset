takahashi_hp, takahashi_power, aoki_hp, aoki_power = map(int, input().split(' '))
takahashi_attack_count = int(aoki_hp / takahashi_power)
if aoki_hp % takahashi_power != 0:
    takahashi_attack_count += 1
aoki_attack_count = int(takahashi_hp / aoki_power)
if takahashi_hp % aoki_power != 0:
    aoki_attack_count += 1

if takahashi_attack_count <= aoki_attack_count:
    print('Yes')
else:
    print('No')