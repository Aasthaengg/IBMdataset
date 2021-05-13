A, B, K = map(int, input().split())
I = []
if A < B:
    C = A
else:
    C = B
for i in range(1, C+1):
    if (A % i == 0) & (B % i == 0):
        I.append(i)
print(I[-K])
