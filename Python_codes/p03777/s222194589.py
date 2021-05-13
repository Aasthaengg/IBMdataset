a, b = input().split()
table = [['H','D'],['D','H']]
ind = ['H','D']
print(table[ind.index(a)][ind.index(b)])