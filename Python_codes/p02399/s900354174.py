list1 = input().split(' ')
list1 = list(map(int, list1))
a = list1[0]
b = list1[1]


ans1 = a // b
ans2 = a % b
ans3 = a / b

print("{0} {1} {2:.6f}".format(ans1, ans2, ans3))