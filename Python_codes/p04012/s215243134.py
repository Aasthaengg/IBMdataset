from collections import defaultdict
s=input()
dd=defaultdict(lambda: True)
for c in s:
  dd[c]=not dd[c]
for k in dd:
  if not dd[k]:
    print("No")
    exit()
print("Yes")