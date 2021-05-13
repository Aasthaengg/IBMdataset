n, t = map(int, input().split())
a = list(map(int, input().split()))
mins = set()
maxs = set()
ma = 0
mi = 10**9
for ind, i in enumerate(a):
    if i<mi:
        mi = i
        min_ind = [ind]
    elif i==mi:
        min_ind.append(ind)
    if i-mi>ma:
        ma = i-mi
        maxs = {ind}
        mins = set(min_ind)
    elif i-mi==ma:
        maxs.add(ind)
        for j in min_ind:
            mins.add(j)
print(min(len(maxs), len(mins)))