from collections import defaultdict
h, w = [int(i) for i in input().split()]
num_count = defaultdict(int)
for i in range(h):
    for j in input():
        num_count[j] += 1
#finish counting

n1 = (h%2) * (w%2)
n2 = h%2 * (w//2)*2 + w%2 * (h//2)*2 # I would have exactly e
n4 = h * w - n1 - n2

for i in num_count:
    while num_count[i] % 4 in [1,3]:
        num_count[i] -= 1
        n1 -= 1
if n1 != 0:
    print("No")
else:
    for i in num_count:
        while num_count[i] % 4  == 2:
            num_count[i] -= 2
            n2 -= 2
    if n2 < 0: #it's ok to have leftover as it can be covered by 4
        print("No")
    else:
        n4 += n2 # those that are not covered yet
        for i in num_count:
            while num_count[i] % 4 == 0 and num_count[i] > 0:
                num_count[i] -= 4
                n4 -= 4
        if n4 != 0:
            print("No")
        else:
            print("Yes")
