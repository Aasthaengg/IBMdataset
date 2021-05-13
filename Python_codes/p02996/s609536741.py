N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
C = list(zip(B, A))
C.sort()
B, A = zip(*C)
t = 0
for c in C:
    t += c[1]
    if t <= c[0]:
        continue
    else:
        print('No')
        exit()
print('Yes')
