from collections import Counter

S=list(input())
count=Counter(S)
for key,cnt in count.most_common():
    if cnt!=1:
        print("no")
        exit()
print("yes")