S = input()

target = list('ACGT')

count_list = [0] * len(S)
for i in range(len(S)):
    if S[i] in target:
        count_list[i] = 1

max_length = 0
for start in range(len(S)):
    if count_list[start] == 0:
        continue
    for end in range(start, len(S)):
        if count_list[end] == 0:
            break

        max_length = max(sum(count_list[start : end+1]), max_length)

print(max_length)