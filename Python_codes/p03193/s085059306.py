n, h, w = map(int, input().split())

li_ita = list()

for _ in range(n):
    li_ita.append(tuple(map(int, input().split())))

print(len(list(filter(lambda x: x[0] >= h and x[1] >= w, li_ita))))