tmp = input().split(" ")

A = int(tmp[0])
B = int(tmp[1])

print(int((A+B)/2)) if (A + B) % 2 == 0 else print("IMPOSSIBLE")