n,m = map(int,input().split())

a_list = []
b_list = []
c_list = []

for a in range(n):
    a_list.append(list(map(int,input().split())))

for b in range(m):
    b_list.append(int(input()))

for c in range(n):
    c_list.append([])
    for d in range(m):
        c_list[c].append((a_list[c][d] * b_list[d]))

c_list = list(map(sum,c_list))

for c in c_list:
    print(c)