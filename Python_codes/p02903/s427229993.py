H, W, A, B = map(int, input().split())

w1 = ''.join(['1'] * A + ['0'] * (W-A))
w2 = ''.join(['0'] * A + ['1'] * (W-A))
for i in range(B):
    print(w1)
for i in range(H-B):
    print(w2)