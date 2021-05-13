n = int(input())
list = input()
count_r = list.count('R')
ans = list[:count_r].count('W')

print(ans)
