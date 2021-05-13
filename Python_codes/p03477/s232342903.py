a, b, c, d = map(int, input().split())
n = a + b - c - d 
if n < 0:
        print('Right')
elif n == 0:
        print('Balanced')
else:
        print('Left')