in_list = input().split(' ')
A = in_list[0]
B = in_list[1]
C = in_list[2]
D = in_list[3]

L = int(A) + int(B)
R = int(C) + int(D)

if L < R:
    print('Right')
elif L > R:
    print('Left')
else:
    print('Balanced')