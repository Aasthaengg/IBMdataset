x, a, b = map(int, input().split())
A =0
B =0

if x<a:
    A = a-x
elif a<x:
    A = x-a
if x<b:
    B = b-x
elif b<x:
    B = x-b
if A<B:
    print("A")
else:
    print("B")
