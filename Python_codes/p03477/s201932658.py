w = list(map(int, input().split()))
l = w[0]+w[1]
r = w[2]+w[3]
if l < r:
    print('Right')
elif l > r:
    print('Left')
else:
    print('Balanced')
