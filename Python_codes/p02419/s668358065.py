from collections import Counter
W=input().lower()
count=0
while True:
    line=input().split()
    if line==["END_OF_TEXT"]:
        break
    count+=Counter(map(lambda x:x.lower(),line))[W]
print(count)