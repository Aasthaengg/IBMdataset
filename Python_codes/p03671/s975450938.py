list = list(map(int, input().split()))*2
print(min(list[0]+list[1], list[1]+list[2], list[2]+list[0]))