from itertools import accumulate, count

n = int(input())

cumsum_ = accumulate(count(1))
cumsum = []
for x in cumsum_:
    if x >= n:
        cumsum.append(x)
        break
    else:
        cumsum.append(x)

x = cumsum[-1] - n
for i in range(1, len(cumsum)+1):
    if i != x:
        print(i)