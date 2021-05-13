n, m = [ int(v) for v in input().split() ]
num_list = [ int(v) for v in input().split() ]
match_table = [2,5,5,4,5,6,3,7,6]
match_table_2 = [ [] for i in range(8) ]
for i in num_list:
    match_table_2[match_table[i-1]].append(i)

match_table_2 = [ (max(match_table_2[i]), i) for i in range(8) if match_table_2[i] != [] ]
match_list, figure_list = zip(*match_table_2)
k = len(match_list)

dp_list = [ 0 for i in range(n+1) ]

for i in range(n+1):
    index_list = [ i - j for j in figure_list ]
    candidate_list = []
    for j in range(k):
        if index_list[j] > 0 and dp_list[index_list[j]] > 0:
            candidate_list.append(dp_list[index_list[j]] * 10 + match_list[j])
        elif index_list[j] == 0:
            candidate_list.append(match_list[j])
    if candidate_list != []:
        dp_list[i] = max(candidate_list)

print(dp_list[-1])