n = int(input())
a = list(map(int,input().split()))

from collections import Counter

z = Counter(a)

i,j,temp = (0,0,0)
for tu in z.items():
    i,j = tu
    if i>j:
        temp+=j
    elif i<j:
        temp+=j-i
    else:
        continue

print(temp)