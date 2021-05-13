a, b = list(map(int, input().split()))

a_height = 0
b_height = 0
sa = abs(a - b)

for i in range(1, sa):
    a_height += i
    
# for i in range(1, sa + 1):
#     b_height += i
    
# print(a_height)
# print(b_height)

print(a_height - a)