S = input()
group = set(S)
count = 0
if len(group) == 2:
    for _ in S:
        if _ == list(group)[0]:
            count += 1

if count == 2:
    print('Yes')
else:
    print('No')