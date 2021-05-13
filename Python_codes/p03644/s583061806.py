N = int(input())
result = []
for i in range(1, N+1):
    bin_i = bin(i)
    bin_i_c = bin_i.count("0")-1
    result.append(bin_i_c)
sorted_result = sorted(result, reverse = True)
print(2 ** sorted_result[0])