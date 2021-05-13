S = input()
result = 10**4
for c in set(S):
    work = []
    temp = 0
    for s in S:
        if s == c:
            work.append(temp)
            temp = 0
        else:
            temp += 1
    work.append(temp)
    result = min(result, max(work))
print(result)