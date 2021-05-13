count = 0

length = int(input())
length_list = list(map(int, input().split()))

for i in range(length - 2):
    for j in range(i + 1, length - 1):
        if length_list[i] != length_list[j]:
            for k in range(j + 1, length):
                if length_list[j] != length_list[k] and length_list[k] != length_list[i]:
                    half_length_sum = (length_list[i] + length_list[j] + length_list[k]) / 2
                    if half_length_sum > max(length_list[i], length_list[j], length_list[k]):
                        count += 1
print(count)