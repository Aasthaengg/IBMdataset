from collections import Counter

s = list(input())

counter = Counter(s)

# print(counter)

for k, v in counter.items():
    if v > 1:
        print("no")
        exit()
print("yes")
