H, W, A, B = map(int, input().split())

a = ['0']*A + ['1'] * (W - A)
b = ['1']*A + ['0'] * (W - A)

for i in range(B):
    print(''.join(a))
for i in range(H-B):
    print(''.join(b))
