def max_benefit(num_list):
    max_num = 10**9*-1
    min_num = num_list[0]

    for i in range(1,len(num_list)):
        max_num = max(max_num,num_list[i]-min_num)
        min_num = min(num_list[i],min_num)
    return max_num

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

ans = max_benefit(num_list)
print(ans)
