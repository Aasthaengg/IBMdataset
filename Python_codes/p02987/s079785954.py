from collections import Counter

s = input()
C = Counter(s)
D = C.most_common()
print("Yes" if len(D) == 2 and D[0][1] == D[1][1] == 2 else "No")