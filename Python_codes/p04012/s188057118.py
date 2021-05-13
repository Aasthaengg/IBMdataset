from collections import Counter
w = input()
counter = Counter(w)
ans = True
for k, v in counter.items():
    if v % 2 == 0:
        continue
    ans = False
    break
if ans:
    print("Yes")
else:
    print("No")