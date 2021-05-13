import collections
S = input()

c = collections.Counter(S)

if len(set(S)) == 2 and c.most_common()[0][1] == 2 and c.most_common()[1][1]:
    print("Yes")
else:
    print("No")