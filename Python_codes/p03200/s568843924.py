s = list(input())
len_s = len(s)
len_b = s.count('B')

b_index_list = []

for i in range(len_s):
    if s[i] == 'B':
        b_index_list.append(i)

b_index_list.reverse()
l0 = len_s - 1
cnt = 0

for b in b_index_list:
    cnt += l0 - b
    l0 -= 1

print(cnt)
