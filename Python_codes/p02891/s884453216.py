S = input()
# A = [int(i) for i in input().split()]
K = int(input())

count_list = []
count = 0
for i in range(len(S)):
    count += 1
    if i == len(S) - 1:
        count_list.append([S[i], count])
        break
    if S[i] != S[i+1]:
        count_list.append([S[i], count])
        count = 0

if len(count_list) == 1:
    print(len(S) * K // 2)
else:
    count = 0
    for _, c in count_list:
        count += c//2
    if count_list[0][0] != count_list[-1][0]:
        print(count * K)
    else:
        head_count = count_list[0][1]
        tail_count = count_list[-1][1]
        mid_change = count - head_count // 2 - tail_count // 2
        con_change = (head_count + tail_count) // 2
        print(head_count // 2 + tail_count // 2 + mid_change * K + con_change * (K-1))
