N, K = map(int, input().split())
A = list(map(int, input().split()))

dict = {}

for a in A:
    if a not in dict:
        dict[a] = 1
    else:
        dict[a] += 1

countlist = sorted([a for a in dict.values()], reverse=True)

print(sum(countlist[K:]))