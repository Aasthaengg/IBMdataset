labels = input().split()
copy = [0, 0, 0, 0, 0, 0]
order = input()
rolls = {'W':[2, 1, 5, 0, 4, 3], 
         'N':[1, 5, 2, 3, 0, 4], 
         'E':[3, 1, 0, 5, 4, 2], 
         'S':[4, 0, 2, 3, 5, 1]
        }
for d in order:
    roll = rolls[d]
    labels = [labels[i] for i in roll]
print(labels[0])
