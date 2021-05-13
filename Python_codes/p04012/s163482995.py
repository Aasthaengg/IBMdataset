from collections import Counter
w = list(input())

cnt = Counter(w)
for i in cnt.values():
  if i%2 == 1:
    print("No")
    exit()
print("Yes")