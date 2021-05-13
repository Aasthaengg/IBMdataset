n = int(input())
stone = input()
r = stone.count("R")
print(stone.count("W", 0, r))