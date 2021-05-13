N, W = map(int, input().split())
w0, v0 = map(int, input().split())
W0 = [0, v0]
W1, W2, W3 = [0], [0], [0]
for i in range(N-1):
    w, v = map(int, input().split())
    if w == w0:
        W0.append(v)
    elif w == w0 + 1:
        W1.append(v)
    elif w == w0 + 2:
        W2.append(v)
    else:
        W3.append(v)
W0.sort()
W1.sort()
W2.sort()
W3.sort()
for i in range(1, len(W0)):
    W0[i] += W0[i-1]
for i in range(1, len(W1)):
    W1[i] += W1[i-1]
for i in range(1, len(W2)):
    W2[i] += W2[i-1]
for i in range(1, len(W3)):
    W3[i] += W3[i-1]

MaxValue = 0
for i in range(len(W0)):
    for j in range(len(W1)):
        for k in range(len(W2)):
            for l in range(len(W3)):
                if w0*i + (w0+1)*j + (w0+2)*k + (w0+3)*l <= W:
                    Total = (W0[-1]-W0[-1-i]) + (W1[-1]-W1[-1-j]) + (W2[-1]-W2[-1-k]) + (W3[-1]-W3[-1-l])
                    MaxValue = max(MaxValue, Total)
print(MaxValue)