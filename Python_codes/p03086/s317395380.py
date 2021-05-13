S = input()
ans_list = []
count = 0
for s in S:
    if s == 'A':
        count += 1
    elif s == 'T':
        count += 1
    elif s == 'G':
        count += 1
    elif s == 'C':
        count += 1
    else:
        count = 0
    ans_list.append(count)
print(max(ans_list))