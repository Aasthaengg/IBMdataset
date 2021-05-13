num_snukes, num_kinds_snack = list(map(int, input().split()))

snack_maps = []

for _ in range(num_kinds_snack):
    num_snukes_has_snack_i = int(input())
    has_snack_list = list(map(int, input().split()))

    snack_maps.append(has_snack_list)

snukes_has_snacks = [False] * num_snukes

for has_snack_list in snack_maps:
    for i in has_snack_list:
        snukes_has_snacks[i - 1] = True

num_victims = len([snuke for snuke in snukes_has_snacks if not snuke])

print(num_victims)
