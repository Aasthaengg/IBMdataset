N = int(input())
stone = input()
R = stone.count('R')
ans = stone.count('W', 0, R)
print(ans)