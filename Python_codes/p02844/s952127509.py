N = int(input())
S = input()

len1 = set()
len2 = set()
len3 = set()

for d in S:
    for l2 in len2:
        len3.add(l2+d)
    for l1 in len1:
        len2.add(l1+d)
    len1.add(d)
print(len(len3))

