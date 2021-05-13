n = int(input())
flame_list = [ int(v) for v in input().split() ]

mean = sum(flame_list)/n

flame_list_2 = [ abs(mean - i) for i in flame_list ]


print(flame_list_2.index(min(flame_list_2)))