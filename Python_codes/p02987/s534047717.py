S=input()
from collections import Counter
c = Counter(list(S))
cnt = 0
for char in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    if c[char] == 2:
        cnt += 1
if cnt == 2:
    print("Yes")
else:
    print("No")