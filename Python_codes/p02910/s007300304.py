S = input()

for i, ch in enumerate(S):
    if i % 2 == 0 and ch == 'L':
        print("No")
        exit()
    elif i % 2 == 1 and ch == 'R':
        print('No')
        exit()    
print("Yes")
