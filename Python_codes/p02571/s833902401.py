S = input()
T = input()

lens = len(S)
lent = len(T)

cur_ans = 999999999999

for i in range(lens - lent + 1):
    local_ans = 0
    for j in range(lent):
        if T[j] != S[i+j]:
            local_ans += 1
    
    cur_ans = min(cur_ans, local_ans)

print(cur_ans)