group = [[1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2]]
x, y = map(int, input().split())
for i in range(3):
    if x in group[i] and y in group[i]:
        print("Yes")
        exit()
    
print("No")