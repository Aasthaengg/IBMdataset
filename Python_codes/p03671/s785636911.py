list = [0, 0, 0]
list[0], list[1], list[2] = map(int, input().split())
list.sort()
print(list[0] + list[1])