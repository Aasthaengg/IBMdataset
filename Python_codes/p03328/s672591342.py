def actual(a, b):
    towers = [1]
    for x in range(2, 999 + 1):
        towers.append(towers[-1] + x)

    for i in range(len(towers)):
        west_tower_height = towers[i]
        east_tower_height = towers[i + 1]

        assert east_tower_height > west_tower_height

        diff = east_tower_height - west_tower_height

        if diff == (b - a):
            return east_tower_height - b

a, b = map(int, input().split())
print(actual(a, b))