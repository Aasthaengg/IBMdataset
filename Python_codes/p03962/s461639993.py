A = input().split(" ")

a = A[0]
b = A[1]
c = A[2]

if a == b and b == c: print(1)
elif a == b or a == c and b != c : print(2)
elif b == c and a != b : print(2)
else : print(3)