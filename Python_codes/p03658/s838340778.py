n = input()
n = n.split(" ")
n = list(map(int, n))
len_ = n[1]

length = input()
length = length.split(" ")
length = list(map(int, length))
length.sort()


length.reverse()
len_max = length[0 : len_]
max_ = sum(len_max)

print(max_)