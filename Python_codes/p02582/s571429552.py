S = input()
count = 0
max_c = 0

for i in S:
    if i != 'R':
        count = 0
    else:
        count = count + 1
    
    if max_c < count:
        max_c = count
    
print(max_c)