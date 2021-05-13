from collections import Counter
w = [c for c in str(input())]
ans = 'Yes'
for k, v in Counter(w).items():
    if v % 2 == 1:
        ans = 'No'
        break
print(ans)