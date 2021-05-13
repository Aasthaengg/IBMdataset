N = int(input())
S = input()

result = 0
for i in range(1, N+1):
    S_forward = S[:i]
    S_backward = S[i:]
    is_same = []
    for j in S_forward:
        if j in S_backward:
            if j not in is_same:
                is_same.append(j)
    result = max(result, len(is_same))

print(result)