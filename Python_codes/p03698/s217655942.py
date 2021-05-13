from collections import Counter
S = input()
l = []
for i in range(len(S)):
    l.append(S[i])
c = Counter(l)
if len(c) == len(S):
    print("yes")
else:
    print("no")
