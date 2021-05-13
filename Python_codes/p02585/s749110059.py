n, k = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

P = [p - 1 for p in P]

def max_point(p, k):
    point = p
    visited = set()
    visited_record = []
    score = 0
    scores = []
    while point not in visited:
        visited.add(point)
        visited_record.append(point)
        score += C[point]
        scores.append(score)
        #update
        point = P[point]
    else:
        loop_entry_index = visited_record.index(point)
        loop_len = len(visited_record) - loop_entry_index
        if loop_entry_index > 0:
            loop_score = scores[-1] - scores[loop_entry_index-1]
        else:
            loop_score = scores[-1]
        head_len = loop_entry_index
    #print(scores)

    if k <= len(scores):
        return max(scores[:k])
    else:
        if loop_score > 0:
            k -= head_len
            scores = scores[:head_len]
            quotient = k // loop_len
            reminder = k % loop_len
            #print(quotient, reminder)
            if scores == []:
                score = 0
            else:
                score = scores[head_len-1]
            score += (quotient - 1) * loop_score
            point = visited_record[loop_entry_index]
            for i in range(loop_len + reminder):
                score += C[point]
                scores.append(score)
                #print(scores, point)
                point = P[point]
            return max(scores)
        else:
            #print(scores)
            return max(scores)

#print(max_point(0, k))

point = -float("inf")
for p in P:
    point = max(max_point(p, k), point)
print(point)
