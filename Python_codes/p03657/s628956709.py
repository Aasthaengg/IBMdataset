A, B = input().split()
A, B = int(A), int(B)
n = int(A) + int(B)
if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
    print('Possible')
else:
    print('Impossible')

   