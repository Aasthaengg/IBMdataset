target = 'ACGT'
S = input()

answer = 0
for start in range(len(S)):
    if S[start] not in target:
        continue
    count = 0
    for end in range(start, len(S)):
        if S[end] not in target:
            break
        count += 1
    
    answer = max(answer, count)

print(answer)