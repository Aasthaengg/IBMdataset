N = int(input())
stones = input()

total_count_R = stones.count('R')
left_count_R = stones[0:total_count_R].count('R')

answer = total_count_R - left_count_R

print(answer)