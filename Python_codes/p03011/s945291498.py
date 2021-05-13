P , Q , R = map(int, input().split())
list = [P , Q , R ]
min1 = min(list)
list.remove(min1)
min2 = min(list)
print(min1 + min2)