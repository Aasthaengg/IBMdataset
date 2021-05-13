from itertools import permutations

a_list = [int(x) for x in input().split()]

ans = sum(a_list)
for temp in list(permutations(a_list)):
    temp_ans = abs(temp[1] - temp[0]) + abs(temp[2] - temp[1])
    if temp_ans < ans:
        ans = temp_ans
print(ans)