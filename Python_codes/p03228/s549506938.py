

A, B, K = (int(i) for i in input().split())  


for i, k in enumerate(range(K)):
    if i % 2 == 0:
        if A % 2 == 1:
            A -= 1
        B += A / 2
        A = A / 2
    
    if i % 2 == 1:
        if B % 2 == 1:
            B -= 1
        A += B / 2
        B = B / 2

print('{} {}'.format(int(A), int(B)))

 



