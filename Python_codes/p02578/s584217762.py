#C
N = int(input())
A = list(map(int, input().split())) 

max_num = 0
sum_num = 0
for i in A:
    max_num =  max(i, max_num)
    calcu_num = max_num
    sum_num += (calcu_num - i)

print(sum_num)