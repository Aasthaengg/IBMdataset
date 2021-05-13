N, K, *AB = map(int, open(0).read().split())
li = [(a, b) for a, b in zip(*[iter(AB)] * 2)]
li.sort()
for a, b in li:
    if K > b:
        K -= b
    else:
        print(a)
        break
