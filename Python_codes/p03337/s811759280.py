A, B = list(map(int, input().split()))
a, b, c = A+B, A-B, A*B
h = [a, b, c]
maxvalue = -10**7
for i in range(len(h)):
    if h[i] > maxvalue:
        maxvalue = h[i]
print(maxvalue)