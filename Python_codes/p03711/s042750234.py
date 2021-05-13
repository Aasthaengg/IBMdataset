a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
z =[a, b, c]
x, y = map(int, input().split())
for i in z:
    if x in i:
        if y in i:
            print("Yes")
            exit()
print("No")
