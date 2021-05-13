p, q, r = map(int,input().split())

min_list = []
min_list.append(p + q) 
min_list.append(r + q)
min_list.append(r + p)

print(min(min_list))