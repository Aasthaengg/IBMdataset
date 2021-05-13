A, B, C, D = map(int, input().split())

weight_left = A + B
weight_right = C + D

if weight_left > weight_right:
    print('Left')
elif weight_left < weight_right:
    print('Right')
else:
    print('Balanced')
