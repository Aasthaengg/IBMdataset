n, m = map(int, input().split())
s = list(input())
s = s[::-1]
ans_list = []

for i in range(n+1):
    if i == 0:
        tmp_count = 0
        tmp_ans = 0
    else:
        tmp_count += 1
        if s[i] == '0':
            tmp_ans = tmp_count
        if tmp_count == m:
            ans_list.append(tmp_ans)
            tmp_count -= tmp_ans
            tmp_ans = tmp_count

if 1 <= tmp_ans <= m:
    ans_list.append(tmp_ans)
if ans_list.count(0) >= 1:
    ans_list = [-1]
    
for i in range(len(ans_list)):
    ans_list[i] = str(ans_list[i])
ans_list = ans_list[::-1]
print(' '.join(ans_list))