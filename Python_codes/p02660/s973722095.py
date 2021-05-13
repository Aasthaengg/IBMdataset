N = int(input())
NN = N
L = []
p = 2
while p <= int(N**0.5):
    if N % p == 0:
        L.append([p])
        N /= p
        while N % p == 0:
            L[-1].append(p)
            N /= p
    p += 1
if N != 1:
    L.append([int(N)])
ans = 0
for i in range(len(L)):
    for j in range(1,len(L[i])+1):
        if NN % (L[i][0])**j == 0:
            NN = NN // (L[i][0])**j
            ans += 1
        else:
            break
print(ans)