ary = input().split(" ")
A = int(ary[0])
B = int(ary[1])

print(A + B) if B % A == 0 else print(B - A)