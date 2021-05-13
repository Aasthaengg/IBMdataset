two_num = input()
two_num = two_num.split(' ')

for i in range(2):
    two_num[i] = int(two_num[i])

if two_num[0] < two_num[1]:
    print("a < b")
elif two_num[0] > two_num[1]:
    print("a > b")
else:
    print("a == b")