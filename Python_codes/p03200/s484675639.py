s = input()
len_s = len(s)
cnt_b = s.count('B')
diff_list = [i for i in range(len_s - cnt_b, len_s)][::-1]
b_idx = []

for idx, el in enumerate(s):
    if el == 'B':
        b_idx.append(idx)
    else:
        pass

total = 0
for pos, idx in zip(diff_list, b_idx):
    total += pos - idx
print(total)
