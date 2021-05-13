X = int(input())

max_num = 1

for bosuu in range(1, 50):
    for sisuu in range(2, 11):
        num = bosuu ** sisuu
        
        if (num <= X):
            max_num = max(max_num, num)
        else:
            break

print(max_num)
