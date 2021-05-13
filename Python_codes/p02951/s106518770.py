water1_limit, water1, water2 = map(int, input().split())

in_water2 = water2 - (water1_limit - water1)
in_water2 = max(0, in_water2)
print(in_water2)
