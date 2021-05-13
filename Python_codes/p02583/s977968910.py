from itertools import combinations

n = int(input())
len_list = list(map(int, input().split()))
len_list = sorted(len_list)
#print(len_list)

per_len = list(combinations(len_list, 3))
#print(per_len)
count = 0

for i in range(len(per_len)):
    if per_len[i][2] == per_len[i][0] or per_len[i][1] == per_len[i][2] or per_len[i][0] == per_len[i][1]:
        pass
    
    else:
        if per_len[i][2] < per_len[i][0] + per_len[i][1] :
            count += 1
            #print(i)
            #print(count)

print(count)