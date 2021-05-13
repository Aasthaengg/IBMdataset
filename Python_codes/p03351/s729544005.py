data_a,data_b,data_c,data_d = [int(x) for x in input().split()]


length_1 = abs(data_a - data_b)
length_2 = abs(data_b - data_c)
length_3 = abs(data_a - data_c)

if length_3 <= data_d:
    print('Yes')
elif length_1 <= data_d and length_2 <= data_d:
    print('Yes')
else:
    print('No')