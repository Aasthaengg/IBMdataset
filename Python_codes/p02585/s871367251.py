n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

# mv_array = [set() for _ in range(n)]
score_mv_array = [[] for _ in range(n)]
score_array = [0]*n

def get_sum(array):
    score_array = [0]
    for i, a in enumerate(array):
        score_array.append(score_array[i]+a)
    return max(score_array)

def get_max(array, q, mod):
    if q == 0:
        m_score = get_sum(array[:mod])
    else:
        m_score = get_sum(array+array[:mod])
        m_score = sum(array)*(q-1) + m_score
    return m_score

for i in range(n):
    score = 0
    max_score = c[i]
    pos = i
    start_pos = p[pos]-1
    for j in range(k):
        pos = p[pos]-1
        # if pos in mv_array[i]:
        if j!=0 and pos == start_pos:
            len_mv = len(score_mv_array[i])
            q, mod = divmod(k-j, len_mv)
            score += get_max(score_mv_array[i], q, mod)
            max_score = max(score, max_score)
            break
        score += c[pos]
        # mv_array[i].add(pos)
        score_mv_array[i].append(c[pos])
        max_score = max(score, max_score)
    score_array[i] = max_score

print(max(score_array))