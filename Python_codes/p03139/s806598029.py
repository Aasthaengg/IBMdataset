# coding: utf-8
# Your code here!

N, A, B = map(int, input().split())

# print(N)
# print(A)
# print(B)

if A < B:
    print(A)
else:
    print(B)
    
# print((A + B) - N)

if ((A + B) - N) >= 0:
    print((A + B) - N)
else:
    print(0)