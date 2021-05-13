a_str, b_str = input().split()
a = int(a_str)
b = int(b_str)

A = a_str*b
B = b_str*a
 
print(min(A, B))