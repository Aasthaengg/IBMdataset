# coding: utf-8
# Your code here!

s = input()

# print(s)

# print(s.find('C'))
# print(s.find('F', 0))

index01 = s.find('C')
index02 = s.find('F', index01)

# print(index01)
# print(index02)

if index01 >= 0 and index02 >= 0:
    print('Yes')
else:
    print('No')