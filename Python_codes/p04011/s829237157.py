n_stay = int(input())
n_p1 = int(input())
p1 = int(input())
p2 = int(input())

print(min([n_p1, n_stay]) * p1 + max([n_stay - n_p1, 0]) * p2)