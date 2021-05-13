a, b = map(int, input().split())
list_a = []
list_b = []

for i in range(a):
    list_a.append(str(b))

for i in range(b):
    list_b.append(str(a))
    
A = ''.join(list_a)
B = ''.join(list_b)

if a >= b:
    print(A)
else:
    print(B)