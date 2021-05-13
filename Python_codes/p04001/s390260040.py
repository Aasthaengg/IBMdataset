S = list(input())
num_cnt = len(S) - 1
total = 0

for i in range(2 ** num_cnt):
    temp_sum = S[0]
    for j in range(num_cnt):
        if ((i >> j) & 1):
            temp_sum = temp_sum + '+' + str(S[j+1])
        else:
            temp_sum = temp_sum  + S[j+1]
    total += eval(temp_sum)

print(total)