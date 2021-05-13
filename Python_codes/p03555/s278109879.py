c_1 = input()
c_2 = input()
rotate_1 = c_1[::-1]
rotate_2 = c_2[::-1]
if c_1 == rotate_2 and c_2 == rotate_1:
    print("YES")
else:
    print("NO")
