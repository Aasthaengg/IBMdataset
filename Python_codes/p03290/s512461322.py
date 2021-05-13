D, G = [int(n) for n in input().split()]

score_table = []
for i in range(1, D+1):
    p, c = [int(n) for n in input().split()]
    score_table.append([i*100, p, c])

min_count = sum([l[1] for l in score_table])
#print(min_count)

for bit in range(1<<D):
    score = 0
    count = 0

    for i in range(D):
        if bit & (1<<i):
            score += score_table[i][0] * score_table[i][1] + score_table[i][2]
            count += score_table[i][1]
    
    if score >= G:
        min_count = min(min_count, count)
    else:
        additional = []
        for j in range(D):
            if not bit & (1<<j):
                additional.append(score_table[j])
        
        additional_ = sorted(additional, key=lambda x:x[0], reverse=True)
        #print(additional_)
        
        # for i in additional_:
        #     if i[1] > 1:
        #         add_score = i
        #         break

        #add_score = additional_[0]

        for k in range(additional_[0][1]-1):
            score += additional_[0][0]
            count += 1
            if score >= G:
                min_count = min(min_count, count)

print(min_count)