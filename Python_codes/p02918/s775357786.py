# N = int(input())
N, K = [int(i) for i in input().split()]
S = input()
count_list = []
pre_s = S[0]
count = 1
for i in range(1, N):
    if S[i] == pre_s:
        count += 1
    else:
        count_list.append([pre_s, count])
        pre_s = S[i]
        count = 1
count_list.append([pre_s, count])

first = S[0]
count = 1
for i in range(1, len(count_list)):
    if count > K:
        break
    if count_list[i][0] != first:
        count_list[i][0] = first
        count += 1

count = count_list[0][1]
next_i = None
for i in range(1, len(count_list)):
    if count_list[i-1][0] == count_list[i][0]:
        count += count_list[i][1]
    else:
        next_i = i
        break

if next_i is not None:
    next_sum = sum([c[1]-1 for c in count_list[next_i:]])
    print(count-1 + next_sum)
else:
    print(count-1)


