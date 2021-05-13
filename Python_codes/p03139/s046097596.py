# PROXY

list = [int(i) for i in input().split()]
print(min(list),(list[1] + list[2]) - list[0] if (list[1] + list[2]) - list[0] > 0 else 0)