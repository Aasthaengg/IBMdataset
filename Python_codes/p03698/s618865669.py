from collections import Counter

s = list(input())
ans = True
for x in Counter(s).values():
    if x > 1:
        ans = False
print(["no", "yes"][ans])
