import collections
i = int(input())
blue = [input() for b in range(i)]
l = int(input())
red = [input() for r in range(l)]
bluecount = collections.Counter(blue)
redcount = collections.Counter(red)

c = 0
for i, j in bluecount.items():
    c = max(j-redcount[i], c)
print(c)
