from itertools import product
s = input()
k = int(input())
anss = []
for bit in product(list(range(len(s)+1)), repeat=2):
    if k >= bit[1] - bit[0] > 0:
        if bit[0] < bit[1] and s[bit[0]:bit[1]] not in anss:
            anss.append(s[bit[0]:bit[1]])

anss.sort()
print(anss[k-1])
