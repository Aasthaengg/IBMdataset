l,r,d = map(int, input().split())
r = r+1
range_list = list(range(l,r))
per_list = []
for i in range_list:
    if i % d == 0:
        per_list.append(i)
    else:
        pass
print(len(per_list))