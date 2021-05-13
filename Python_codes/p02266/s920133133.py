ch = input()
area_idx = []
area = []
for i, c in enumerate(ch):
    if c == '\\':
        area_idx.append(i)
    elif c == '/' and area_idx:
        j = area_idx.pop() 
        v = i-j
        while area and j < area[-1][0]:
            v += area.pop()[1]
        area.append((j, v))
n = len(area)
a = [v[1] for v in area]
print(sum(a))
print(n, *a)
