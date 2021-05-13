s = list(input())

s_set = set(s)

cnt = 101
for l in s_set:
    indexs = set([i for i, x in enumerate(s) if x == l])
    i = len(s)
    while len(indexs) < i:
        indexsList = list(indexs)
        for j in range(len(indexs)):
            n = indexsList[j]
            if n == 0:
                pass
            elif n == i - 1:
                indexs.remove(n)
                indexs.add(n-1)
            else:
                indexs.add(n-1)
        i -= 1
    cnt = min(cnt, len(s)-i)

print(cnt)