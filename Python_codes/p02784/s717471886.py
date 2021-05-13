hp,sp = input().split(" ")
hp = int(hp)
sp = int(sp)
attack = input().split(" ")
damage = 0

for i, new in enumerate(attack):
    attack[i] = int(attack[i])

for i in range(0,sp):
    damage += attack[i]

if damage >= hp:
    print("Yes")

else:
    print("No")