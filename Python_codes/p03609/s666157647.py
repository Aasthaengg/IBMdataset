sand_weight, drop_sand_per_second = map(int, input().split())

if sand_weight > drop_sand_per_second:
    remain_sand = sand_weight - drop_sand_per_second
    print(remain_sand)
else:
    print(0)