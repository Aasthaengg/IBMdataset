list_a = [[int(n) for n in input().split()] for m in range(0, 3)]
n = int(input())
list_b = [int(input()) for k in range(0, n)]

if (list_a[0][0] in list_b and list_a[0][1] in list_b and list_a[0][2] in list_b) or\
    (list_a[1][0] in list_b and list_a[1][1] in list_b and list_a[1][2] in list_b) or\
    (list_a[2][0] in list_b and list_a[2][1] in list_b and list_a[2][2] in list_b) :
    print('Yes')

elif (list_a[0][0] in list_b and list_a[1][0] in list_b and list_a[2][0] in list_b) or\
    (list_a[0][1] in list_b and list_a[1][1] in list_b and list_a[2][1] in list_b) or\
    (list_a[0][2] in list_b and list_a[1][2] in list_b and list_a[2][2] in list_b) :
    print('Yes')

elif (list_a[0][0] in list_b and list_a[1][1] in list_b and list_a[2][2] in list_b) or\
    (list_a[2][0] in list_b and list_a[1][1] in list_b and list_a[0][2] in list_b):
    print('Yes')

else:
    print('No')