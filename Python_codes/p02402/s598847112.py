input()
n_list = []
for n in map(int, input().split()):
    n_list.append(n)
print(min(n_list), max(n_list), sum(n_list))

