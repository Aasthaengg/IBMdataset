n = int(input())
sum_min = 100000
for i in range(1,n):
    i_sum = 0; j_sum = 0
    j = n-i
    i = str(i); j = str(j)
    for k in range(len(i)):
        i_sum += int(i[k])
    for k in range(len(j)):
        j_sum += int(j[k])
    tmp_sum  = i_sum + j_sum
    if sum_min >tmp_sum :
        sum_min = tmp_sum
print(sum_min)