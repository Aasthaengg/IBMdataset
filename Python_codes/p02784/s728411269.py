#   アライグマ対モンスター

#   入力
hp_m, n = map(int, input().split())
attack = list(map(int, input().split()))

total_attack = sum(attack)

if total_attack >= hp_m:
    print("Yes")
else:
    print("No")
