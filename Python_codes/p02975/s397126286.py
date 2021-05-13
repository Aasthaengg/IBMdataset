N = input()
a_list = [int(_c) for _c in input().split(" ")]

xor = 0
for a in a_list:
    xor = xor ^ a

if xor == 0:
    print("Yes")
else:
    print("No")