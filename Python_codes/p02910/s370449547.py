S = input()
odds = []
evens = []
for i in range(len(S)):
    if i % 2 == 0:
        odds.append(S[i])
    else:
        evens.append(S[i])

if 'L' not in odds and 'R' not in evens:
    print('Yes')
else:
    print('No')